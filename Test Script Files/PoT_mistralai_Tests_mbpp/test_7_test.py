import unittest
from mbpp_7_code import find_char_long

class TestFindCharLong(unittest.TestCase):
    def test_typical_case(self):
        self.assertListEqual(find_char_long("Hello World"), ["Hello", "World"])

    def test_edge_case_short_string(self):
        self.assertListEqual(find_char_long("abcd"), ["abcd"])

    def test_edge_case_long_string(self):
        self.assertListEqual(find_char_long("a" * 100), ["a" * 4, "a" * 100])

    def test_edge_case_single_word(self):
        self.assertListEqual(find_char_long("word"), ["word"])

    def test_edge_case_empty_string(self):
        self.assertListEqual(find_char_long(""), [])

    def test_edge_case_only_numbers(self):
        self.assertListEqual(find_char_long("1234"), [])

    def test_edge_case_only_special_characters(self):
        self.assertListEqual(find_char_long("!@#$%^&*()"), [])

    def test_edge_case_only_spaces(self):
        self.assertListEqual(find_char_long("   "), [])

    def test_corner_case_single_word_with_hyphen(self):
        self.assertListEqual(find_char_long("word-"), ["word"])
