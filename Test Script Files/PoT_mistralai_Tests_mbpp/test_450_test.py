import unittest
from mbpp_450_code import extract_string

class TestExtractString(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(extract_string("abcdefg", 3), ["abc", "def"])
        self.assertEqual(extract_string("123456", 2), ["12", "34", "56"])

    def test_edge_case_empty_string(self):
        self.assertEqual(extract_string("", 3), [])

    def test_edge_case_single_char(self):
        self.assertEqual(extract_string("a", 1), ["a"])
        self.assertEqual(extract_string("a", 2), [])

    def test_edge_case_single_word(self):
        self.assertEqual(extract_string("word", 4), ["word"])
        self.assertEqual(extract_string("word", 5), [])

    def test_edge_case_single_digit(self):
        self.assertEqual(extract_string("1", 1), ["1"])
        self.assertEqual(extract_string("1", 2), [])
