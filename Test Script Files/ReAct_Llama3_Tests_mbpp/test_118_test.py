import unittest
from mbpp_118_code import string_to_list

class TestStringToList(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(string_to_list(""), [])

    def test_single_word(self):
        self.assertEqual(string_to_list("hello"), ["hello"])

    def test_multiple_words(self):
        self.assertEqual(string_to_list("hello world"), ["hello", "world"])

    def test_multiple_spaces(self):
        self.assertEqual(string_to_list("hello   world"), ["hello", "world"])

    def test_leading_trailing_spaces(self):
        self.assertEqual(string_to_list("   hello   world   "), ["hello", "world"])

    def test_empty_string_with_spaces(self):
        self.assertEqual(string_to_list("   "), [])

    def test_non_string_input(self):
        with self.assertRaises(TypeError):
            string_to_list(123)

    def test_non_string_input_with_spaces(self):
        with self.assertRaises(TypeError):
            string_to_list("123   ")
