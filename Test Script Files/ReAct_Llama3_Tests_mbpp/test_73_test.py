import unittest
from mbpp_73_code import multiple_split

class TestMultipleSplit(unittest.TestCase):

    def test_typical_split(self):
        self.assertEqual(multiple_split("Hello; World, this is a test *test*"), ["Hello", " World, this is a test *test*"])

    def test_edge_case_empty_string(self):
        self.assertEqual(multiple_split(""), [])

    def test_edge_case_single_separator(self):
        self.assertEqual(multiple_split("Hello;"), ["Hello"])

    def test_edge_case_multiple_separators(self):
        self.assertEqual(multiple_split("Hello; World, this is a test *test*; another test"), ["Hello", " World, this is a test *test*", "another test"])

    def test_edge_case_separator_at_end(self):
        self.assertEqual(multiple_split("Hello; World, this is a test *test*;"), ["Hello", " World, this is a test *test*"])

    def test_edge_case_separator_at_start(self):
        self.assertEqual(multiple_split("; World, this is a test *test* Hello"), ["", " World, this is a test *test* Hello"])

    def test_edge_case_separator_in_middle(self):
        self.assertEqual(multiple_split("Hello; World, this is a test *test*; another test;"), ["Hello", " World, this is a test *test*", " another test"])

    def test_edge_case_separator_at_start_and_end(self):
        self.assertEqual(multiple_split("; World, this is a test *test* ;"), ["", " World, this is a test *test* "])

    def test_edge_case_separator_in_middle_and_end(self):
        self.assertEqual(multiple_split("Hello; World, this is a test *test*; another test ;"), ["Hello", " World, this is a test *test*", " another test"])
