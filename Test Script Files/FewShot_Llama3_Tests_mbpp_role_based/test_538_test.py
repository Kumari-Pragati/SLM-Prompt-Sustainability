import unittest
from mbpp_538_code import string_list_to_tuple

class TestStringListToTuple(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(string_list_to_tuple(""), ())

    def test_single_word(self):
        self.assertEqual(string_list_to_tuple("hello"), ("hello",))

    def test_multiple_words(self):
        self.assertEqual(string_list_to_tuple("hello world"), ("hello", "world"))

    def test_spaces_between_words(self):
        self.assertEqual(string_list_to_tuple("hello  world"), ("hello", "world"))

    def test_spaces_at_beginning_and_end(self):
        self.assertEqual(string_list_to_tuple("   hello   world   "), ("hello", "world"))

    def test_spaces_and_newlines(self):
        self.assertEqual(string_list_to_tuple("hello\nworld"), ("hello", "world"))

    def test_non_space_characters(self):
        self.assertEqual(string_list_to_tuple("hello world!"), ("hello", "world"))
