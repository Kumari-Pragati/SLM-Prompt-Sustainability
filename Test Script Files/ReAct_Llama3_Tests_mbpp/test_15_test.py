import unittest
from mbpp_15_code import split_lowerstring

class TestSplitLowerstring(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(split_lowerstring("hello world"), ["hello", "world"])

    def test_edge_case_empty_string(self):
        self.assertEqual(split_lowerstring(""), [])

    def test_edge_case_single_char(self):
        self.assertEqual(split_lowerstring("a"), ["a"])

    def test_edge_case_single_word(self):
        self.assertEqual(split_lowerstring("hello"), ["hello"])

    def test_edge_case_multiple_words(self):
        self.assertEqual(split_lowerstring("hello world foo bar"), ["hello", "world", "foo", "bar"])

    def test_edge_case_non_alphabetic_chars(self):
        self.assertEqual(split_lowerstring("hello!world"), ["hello", "world"])

    def test_edge_case_non_alphabetic_chars_at_start(self):
        self.assertEqual(split_lowerstring("!hello world"), ["hello", "world"])

    def test_edge_case_non_alphabetic_chars_at_end(self):
        self.assertEqual(split_lowerstring("hello world!"), ["hello", "world"])

    def test_edge_case_non_alphabetic_chars_in_between(self):
        self.assertEqual(split_lowerstring("hello!world!foo"), ["hello", "world", "foo"])
