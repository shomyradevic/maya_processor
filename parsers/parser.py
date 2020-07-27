from __future__ import (
    print_function,
    #unicode_literals
)
from os import listdir, path


class Pipe:

    def __init__(self, files_folder):
        self.files_folder = files_folder

    def generator(self):
        """
        :return: (
            Just yields every line from passed directory path in constructor.
            Existence checking has already been done.
        )
        """
        for file_path in listdir(self.files_folder):
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

    def start(self):
        """
        Main function that runs the parsing process.
        :return: None
        """
        begin_pattern, end_pattern = 'createNode mesh ', 'createNode '
        bn, en = len(begin_pattern) + 1, len(end_pattern) + 1
        begin = False

        parsed_meshes = []
        mesh_description = ''

        for line in self.pipeline.generator():
            if begin:
                if line.find(end_pattern, 0, en) >= 0:
                    begin = False
                    parsed_meshes.append(self.partial_mesh_parse(mesh_description))
                    mesh_description = ''
                else:
                    mesh_description += line
            elif line.find(begin_pattern, 0, bn) >= 0:
                begin = True
                mesh_description += line

    def partial_mesh_parse(self, mesh):
        """
        :param mesh: String representation of specific mesh object.
        :return: None
        """
        n = len(mesh)
        data = dict()
        data["name"] = self.get_name(mesh=mesh, n=n)
        print("Found name: " + str(data["name"]))

    def get_name(self, mesh, n):
        begin_pattern, end_pattern = " mesh -n ", "-p"
        i = mesh.find(begin_pattern, 0, n)

        if i == -1:
            return None
        else:
            i += len(begin_pattern)  # Name is after our pattern

        j = mesh.find(end_pattern, i, n)

        if j == -1:
            return None
        else:
            return mesh[i + 1:j - 2]

    def get_uid(self, mesh):
        pass

    def get_position(self, mesh):
        pass



if __name__ == '__main__':
    #a = [5, 2, 3, 4]
    #b = tuple(a)
    #d = {'a': b}
    #print(d)
    Parser(files_folder="..\\proba").start()