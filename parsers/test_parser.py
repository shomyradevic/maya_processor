from __future__ import (
    #unicode_literals,
    print_function
)
import unittest
from .parser import Parser


class ParserTest(unittest.TestCase):

    def setUp(self):
        self.parser = Parser(files_folder="example_files")

    def control(self, test_cases, function_with_args):
        for case in test_cases:
            parsed_result = eval(function_with_args)
            self.assertEqual(parsed_result, case["output"])

    #def test_parse(self):
        #instance = Parser(files_folder="..\\wrong_path")
        #instance.parse()

    def tearDown(self):
        pass

    def test_get_name(self):
        test_cases = (
            {
                "input": " ",
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
            function_with_args="self.parser.get_name(mesh=case[\"input\"], n=len(case[\"input\"]))"
        )

    def test_get_uid(self):
        test_cases = (
            {
                "input": " ",
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
            function_with_args="self.parser.get_uid(mesh=case[\"input\"], n=len(case[\"input\"]))"
        )

    def test_get_position(self):
        test_cases = (
            {
                "input": " ",
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
            function_with_args="self.parser.get_name(mesh=case[\"input\"], n=len(case[\"input\"]))"
        )


if __name__ == '__main__':
    unittest.main()