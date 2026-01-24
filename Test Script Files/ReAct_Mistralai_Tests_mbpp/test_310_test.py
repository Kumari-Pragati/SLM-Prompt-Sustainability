import unittest
from mbpp_310_code import string_to_tuple

class TestStringToTuple(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(string_to_tuple(""), tuple())

    def test_single_character(self):
        for char in "abcdefghijklmnopqrstuvwxyz":
            self.assertEqual(string_to_tuple(char), (char,))

    def test_multiple_characters(self):
        self.assertEqual(string_to_tuple("hello"), ("h", "e", "l", "l", "o"))

    def test_leading_trailing_spaces(self):
        self.assertEqual(string_to_tuple("  hello  "), ("h", "e", "l", "l", "o"))

    def test_only_spaces(self):
        self.assertEqual(string_to_tuple("   "), ())

    def test_mixed_spaces_and_characters(self):
        self.assertEqual(string_to_tuple("  hello, world!  "), ("h", "e", "l", "l", "o", ","))

    def test_non_string_input(self):
        with self.assertRaises(TypeError):
            string_to_tuple(123)
