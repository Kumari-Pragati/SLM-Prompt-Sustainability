import unittest
from118_code import string_to_list

class TestStringToList(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(string_to_list(""), [])

    def test_single_word(self):
        self.assertEqual(string_to_list("hello"), ["hello"])

    def test_multiple_words(self):
        self.assertEqual(string_to_list("hello world"), ["hello", "world"])

    def test_whitespace_only(self):
        self.assertEqual(string_to_list("   "), [""])

    def test_leading_trailing_whitespace(self):
        self.assertEqual(string_to_list(" hello world "), ["hello", "world"])

    def test_punctuation_in_word(self):
        self.assertEqual(string_to_list("hello,world"), ["hello", ",", "world"])

    def test_multiple_punctuation(self):
        self.assertEqual(string_to_list("hello.,,world"), ["hello", ",", ",", "world"])

    def test_non_alphanumeric_characters(self):
        self.assertEqual(string_to_list("hello#world"), ["hello", "#", "world"])

    def test_invalid_input(self):
        self.assertRaises(TypeError, string_to_list, 123)
