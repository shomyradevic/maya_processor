from __future__ import print_function
from parsers.parser import Parser


def new(memory, new_line):
    return memory[1:] + [new_line]


test_cases = (
            {
                "input": " ",
                "output": None
            },
            {
                "input": "rename -uid \"13C79C5C-402E-63DE-D388-53B66872D238\";",
                "output": "13C79C5C-402E-63DE-D388-53B66872D238"
            },
            {
                "input": "rename -uid \"13C79C5C-402E-63DE-D388-53B66872D238\"",
                "output": None
            },
            {
                "input": "rename uid \"13C79C5C-402E-63DE-D388-53B66872D238\";",
                "output": None
            }
        )


def get_uid(mesh, n):
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


if __name__ == '__main__':
    ex = "rename -uid \"9BC8DE79-468E-8469-0D05-C19729563BCC\";"
    call = "get_uid(mesh=ex, n=len(ex))"
    result = eval(call)
    print(result)


    """counter = 0
    for case in test_cases:
        counter += 1
        parsed_result = p.get_uid(mesh=case["input"], n=len(case["input"]))
        print(counter)
        print(parsed_result)"""