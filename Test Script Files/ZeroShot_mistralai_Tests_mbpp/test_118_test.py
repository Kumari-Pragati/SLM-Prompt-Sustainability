import unittest
from mbpp_118_code import string_to_list

class TestStringToList(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(string_to_list(""), [])

    def test_single_word_string(self):
        self.assertEqual(string_to_list("hello"), ["hello"])

    def test_multiple_words_string(self):
        self.assertEqual(string_to_list("hello world"), ["hello", "world"])

    def test_whitespace_only_string(self):
        self.assertEqual(string_to_list("   "), [""])

    def test_string_with_leading_trailing_whitespace(self):
        self.assertEqual(string_to_list(" hello world   "), ["hello", "world"])

    def test_string_with_multiple_spaces(self):
        self.assertEqual(string_to_list("hello   world"), ["hello", "world"])

    def test_string_with_non_space_characters(self):
        self.assertRaises(ValueError, string_to_list, "hello123world")
