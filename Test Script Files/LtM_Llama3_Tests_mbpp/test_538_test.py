import unittest
from mbpp_538_code import string_list_to_tuple

class TestStringListToTuple(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(string_list_to_tuple(""), ())
    def test_single_space(self):
        self.assertEqual(string_list_to_tuple(" "), ())
    def test_multiple_spaces(self):
        self.assertEqual(string_list_to_tuple("   "), ())
    def test_single_word(self):
        self.assertEqual(string_list_to_tuple("hello"), ("hello",))
    def test_multiple_words(self):
        self.assertEqual(string_list_to_tuple("hello world"), ("hello", "world"))
    def test_mixed_spaces_and_words(self):
        self.assertEqual(string_list_to_tuple("hello  world"), ("hello", "world"))
    def test_empty_string_with_spaces(self):
        self.assertEqual(string_list_to_tuple("   "), ())
    def test_string_with_leading_spaces(self):
        self.assertEqual(string_list_to_tuple("   hello"), ("hello",))
    def test_string_with_trailing_spaces(self):
        self.assertEqual(string_list_to_tuple("hello   "), ("hello",))
