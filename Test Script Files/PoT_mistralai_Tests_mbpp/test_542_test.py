import unittest
from mbpp_542_code import fill_spaces

class TestFillSpaces(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(fill_spaces("hello, world. This is a test."), "hello:world. This:is:a:test.")

    def test_edge_case_single_space(self):
        self.assertEqual(fill_spaces("hello world"), "hello:world")

    def test_edge_case_no_spaces(self):
        self.assertEqual(fill_spaces("helloworld"), "helloworld")

    def test_edge_case_single_char(self):
        self.assertEqual(fill_spaces("h"), ":h")

    def test_edge_case_empty_string(self):
        self.assertEqual(fill_spaces(""), "")

    def test_corner_case_multiple_punctuation(self):
        self.assertEqual(fill_spaces("hello, world! This is a test?"), "hello:world! This:is:a:test?")
