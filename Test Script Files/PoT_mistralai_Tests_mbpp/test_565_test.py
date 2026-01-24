import unittest
from mbpp_565_code import split

class TestSplitFunction(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(split("hello"), ["h", "e", "l", "l", "o"])

    def test_edge_case_empty_string(self):
        self.assertEqual(split(""), [])

    def test_edge_case_single_char(self):
        self.assertEqual(split("a"), ["a"])

    def test_edge_case_whitespace(self):
        self.assertEqual(split(" "), [" "])
        self.assertEqual(split("\t"), ["\t"])

    def test_boundary_case_long_string(self):
        long_string = "a" * 100
        self.assertEqual(len(split(long_string)), 100)
