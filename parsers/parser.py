from __future__ import (
    print_function,
)
from os import listdir, path


class Pipe:

    def __init__(self, files_folder):
        self.files_folder = files_folder

    def generator(self):
        """
        :return: (
            Yields every line from each .ma file from passed directory path in constructor.
            Existence checking has already been done.
        )
        """
        for file_path in listdir(self.files_folder):
            if path.splitext(file_path)[1] == '.ma':
                descriptor = open(path.join(self.files_folder, file_path), mode="r")
                for line in descriptor:
                    yield line
                descriptor.close()


class Parser:

    def __init__(self, files_folder):
        """
        :param files_folder: Directory path where all the maya files are located
        """
        if not path.isdir(files_folder):
            raise SystemExit("Passed argument is not a directory.")

        self.pipeline = Pipe(files_folder=files_folder)

    def parse(self):
        """
        Main function that runs the parsing process.
        :return: None
        """
        begin_pattern, end_pattern = 'createNode mesh ', 'createNode '
        bn, en = len(begin_pattern) + 1, len(end_pattern) + 1
        begin = False

        parsed_meshes = []
        mesh_description = ''

        last_3 = ['', '', '']

        for line in self.pipeline.generator():
            if begin:
                if line.find(end_pattern, 0, en) >= 0:  # We found a Mesh object
                    begin = False
                    fresh_mesh = self.partial_mesh_parse(mesh_description, last_3)
                    parsed_meshes.append(fresh_mesh)
                    mesh_description = ''
                else:
                    mesh_description += line
            else:
                last_3 = last_3[1:] + [line]

            if line.find(begin_pattern, 0, bn) >= 0:
                begin = True
                mesh_description += line

        [print(mesh) for mesh in parsed_meshes]

    def partial_mesh_parse(self, mesh, last_3):
        """
        :param mesh: String representation of specific mesh object.
        :param: last_3: List of last 3 lines. For position needs.
        :return: Dictionary represented Mesh object.
        """
        n = len(mesh)
        data = dict()
        data["name"] = self.get_name(mesh=mesh, n=n)
        data["uid"] = self.get_uid(mesh=mesh, n=n)
        data["position"] = self.get_position(last_3=last_3)
        return data

    def get_name(self, mesh, n):
        """
        :param mesh: Mesh string
        :return: Name or None
        """
        begin_pattern, end_pattern = " mesh -n ", "-p"
        i = mesh.find(begin_pattern, 0, n)

        if i == -1:
            return None
        i += len(begin_pattern)  # Name is after our pattern

        j = mesh.find(end_pattern, i, n)

        if j == -1:
            return None
        return mesh[i + 1:j - 2]

    def get_uid(self, mesh, n):
        """
        :param mesh: Mesh string
        :return: Uid or None
        """
        begin_pattern, end_pattern = " -uid ", ";"
        i = mesh.find(begin_pattern, 0, n)

        if i == -1:
            return None
        i += len(begin_pattern)

        j = mesh.find(end_pattern, i, n)

        if j == -1:
            return None
        return mesh[i + 1:j - 1]

    def get_position(self, last_3):
        """
        :param last_3: List of last 3 lines.
        :return: tuple of positions or None.
        """
        begin_pattern, end_pattern = "setAttr \".t\" -type \"double3\"", ";"
        for line in last_3:
            i = line.find(begin_pattern, 0, len(line))
            if i >= 0:
                i += len(begin_pattern)
                j = line.find(end_pattern, i, len(line))
                if j >= i:
                    return tuple(line[i:j].strip().split())


if __name__ == '__main__':
    Parser(files_folder="..\\example_files").parse()
