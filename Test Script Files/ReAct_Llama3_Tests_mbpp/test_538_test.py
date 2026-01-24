import unittest
from mbpp_538_code import string_list_to_tuple

class TestStringListToTuple(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(string_list_to_tuple(""), ())

    def test_single_word(self):
        self.assertEqual(string_list_to_tuple("hello"), ("hello",))

    def test_multiple_words(self):
        self.assertEqual(string_list_to_tuple("hello world"), ("hello", "world"))

    def test_empty_string_with_spaces(self):
        self.assertEqual(string_list_to_tuple("   "), ())

    def test_string_with_leading_trailing_spaces(self):
        self.assertEqual(string_list_to_tuple("   hello   "), ("hello",))

    def test_string_with_spaces_and_punctuation(self):
        self.assertEqual(string_list_to_tuple("hello, world!"), ("hello", "world"))

    def test_string_with_leading_trailing_punctuation(self):
        self.assertEqual(string_list_to_tuple("!, hello, world!"), ("hello", "world"))

    def test_string_with_leading_trailing_spaces_and_punctuation(self):
        self.assertEqual(string_list_to_tuple("  !, hello, world!   "), ("hello", "world"))

    def test_string_with_non_space_characters(self):
        self.assertEqual(string_list_to_tuple("hello123"), ("hello123",))

    def test_string_with_non_space_characters_and_punctuation(self):
        self.assertEqual(string_list_to_tuple("hello123, world!"), ("hello123", "world"))
