from __future__ import (
    unicode_literals,
    print_function
)
import unittest
from .parser import Pipe


class ParserTest(unittest.TestCase):

    def setUp(self):
        self.pipeline = Pipe(files_folder="..\\eexample_files")

    def tearDown(self):
        pass

    def test_generator(self):
        self.assertIsInstance(self.pipeline.generator, str)


if __name__ == '__main__':
    unittest.main()