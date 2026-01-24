import unittest
from mbpp_647_code import split_upperstring

class TestSplitUpperstring(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(split_upperstring("HelloWorld"), ["Hello", "World"])

    def test_edge_case_empty_string(self):
        self.assertEqual(split_upperstring(""), [])

    def test_edge_case_single_uppercase(self):
        self.assertEqual(split_upperstring("A"), ["A"])

    def test_edge_case_single_lowercase(self):
        self.assertEqual(split_upperstring("a"), [])

    def test_edge_case_multiple_uppercase(self):
        self.assertEqual(split_upperstring("ABC"), ["ABC"])

    def test_edge_case_multiple_lowercase(self):
        self.assertEqual(split_upperstring("abc"), [])

    def test_edge_case_mixed_case(self):
        self.assertEqual(split_upperstring("AbC"), ["Ab", "C"])

    def test_edge_case_punctuation(self):
        self.assertEqual(split_upperstring("Hello,World!"), ["Hello", "World"])

    def test_edge_case_numbers(self):
        self.assertEqual(split_upperstring("Hello123World"), ["Hello", "World"])

    def test_edge_case_spaces(self):
        self.assertEqual(split_upperstring("Hello World"), ["Hello", "World"])

    def test_edge_case_newline(self):
        self.assertEqual(split_upperstring("Hello\nWorld"), ["Hello", "World"])
