from __future__ import (
    #unicode_literals,
    print_function
)
import unittest
from parsers.parser import Parser


class ParserTest(unittest.TestCase):
    """
    Some of the test cases are questionable, the best practice in my opinion would be to interface with
    employees that are responsible for generating .ma files, to see what are possible corner cases,
    as well as regular test cases.
    """

    @classmethod
    def setUpClass(cls):
        """
        We are using this class variable during entire testing.
        """
        ParserTest.parser = Parser(files_folder="example_files")

    def control(self, test_cases, function_with_args):
        """
        :param test_cases: Lists of dictionaries. One dictionary holds the
        function input and expected output.
        :param function_with_args: Callable string.
        :return:
        """
        for case in test_cases:
            parsed_result = eval(function_with_args)
            self.assertEqual(parsed_result, case["output"])

    def test_parse(self):
        instance = None
        try:
            instance = Parser(files_folder="..\\wrong_path\\to\\files_folder")
        except SystemExit:
            pass
        finally:
            self.assertEqual(instance, None)

    def test_get_name(self):
        test_cases = (
            {
                "input": "",
                "output": None
            },
            {
                "input": "createNode mesh -n \"CubeShape\" -p \"Cube\"",
                "output": "CubeShape"
            },
            {
                "input": "createNode transform -n \"Cube\"; \
                        rename -uid \"8690CE34-4E5E-1275-5747-F8A21428D67B\"; \
                        setAttr \".t\" -type \"double3\" -3 2 2 ; \
                        createNode mesh -n \"CubeShape\" -p \"Cube\";",
                "output": "CubeShape"
            },
            {
                "input": "createNode mesh \"Cube\" -p",
                "output": None
            },
            {
                "input": "createNode mesh -n \"Sphere\"",
                "output": None
            }
        )
        self.control(
            test_cases=test_cases,
            function_with_args="ParserTest.parser.get_name(mesh=case[\"input\"], n=len(case[\"input\"]))"
        )

    def test_get_uid(self):
        test_cases = (
            {
                "input": "",
                "output": None
            },
            {
                "input": "rename -uid \"9BC8DE79-468E-8469-0D05-C19729563BCC\";",
                "output": "9BC8DE79-468E-8469-0D05-C19729563BCC"
            },
            {
                "input": "rename -uid \"47C059BB-4D70-AC70-532B-38A9A7C92F68\"",
                "output": None
            },
            {
                "input": "rename uid \"14C79C5C-402E-63DE-D388-53B66872D238\";",
                "output": None
            }
        )
        self.control(
            test_cases=test_cases,
            function_with_args="ParserTest.parser.get_uid(mesh=case[\"input\"], n=len(case[\"input\"]))"
        )

    def test_get_position(self):
        test_cases = (
            {
                "input": ['', '', ''],
                "output": None
            },
            {
                "input": ["\0", "setAttr \".t\" -type \"double3\" -3 2 2 ;", "\0"],
                "output": ('-3', '2', '2')
            },
            {
                "input": ["setAttr \".t\" -type \"double2\" -3 2 2 ;"],
                "output": None
            },
            {
                "input": ["string"*100, "createNode transform -n \"Torus\"; \
                            rename -uid \"6CA7FB06-409E-DADE-2932-68B89130D104\"; \
                            setAttr \".t\" -type \"double3\" -9.7245613999699021 3.5468205018979577 -3.4691659115871456 ; \
                            createNode mesh -n \"TorusShape\" -p \"Torus\";", "string"*100],
                "output": ('-9.7245613999699021', '3.5468205018979577', '-3.4691659115871456')
            }
        )
        self.control(
            test_cases=test_cases,
            function_with_args="ParserTest.parser.get_position(last_3=case[\"input\"])"
        )


if __name__ == '__main__':
    unittest.main()