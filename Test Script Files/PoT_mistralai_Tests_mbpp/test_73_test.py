import unittest
from mbpp_73_code import multiple_split

class TestMultipleSplit(unittest.TestCase):

    def test_typical_case(self):
        self.assertListEqual(multiple_split("a;b,c*d\ne"), ["a", "b", "c", "d", "e"])
        self.assertListEqual(multiple_split("a; b, c* d\ne"), ["a", "b", "c", "d", "e"])
        self.assertListEqual(multiple_split("a; b, c*d\n e"), ["a", "b", "c", "d", "e"])

    def test_edge_case_empty_string(self):
        self.assertListEqual(multiple_split(""), [])

    def test_edge_case_single_element(self):
        self.assertListEqual(multiple_split("a"), ["a"])

    def test_edge_case_single_char(self):
        self.assertListEqual(multiple_split("a;"), ["a"])
        self.assertListEqual(multiple_split(";a"), [""])
        self.assertListEqual(multiple_split(";"), [])
        self.assertListEqual(multiple_split(","), [])
        self.assertListEqual(multiple_split("*"), [])
        self.assertListEqual(multiple_split("\n"), [])

    def test_edge_case_multiple_newlines(self):
        self.assertListEqual(multiple_split("\na\nb"), ["a", "b"])
        self.assertListEqual(multiple_split("\na\n\nb"), ["a", "b"])

    def test_edge_case_escaped_characters(self):
        self.assertListEqual(multiple_split("a;b,c*d\\ne"), ["a", "b", "c", "d", "e"])

    def test_edge_case_trailing_newline(self):
        self.assertListEqual(multiple_split("a;b,c*d\ne\n"), ["a", "b", "c", "d", "e"])

    def test_edge_case_leading_newline(self):
        self.assertListEqual(multiple_split("\na;b,c*d\ne"), ["a", "b", "c", "d", "e"])

    def test_corner_case_escaped_newline(self):
        self.assertListEqual(multiple_split("a;b,c*d\\ne\\n"), ["a", "b", "c", "d"])
