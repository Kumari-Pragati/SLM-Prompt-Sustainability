import unittest
from mbpp_813_code import string_length

class TestStringLength(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(string_length("hello"), 5)

    def test_empty_string(self):
        self.assertEqual(string_length(""), 0)

    def test_single_character(self):
        self.assertEqual(string_length("a"), 1)

    def test_multiple_spaces(self):
        self.assertEqual(string_length("   "), 3)

    def test_non_string_input(self):
        with self.assertRaises(TypeError):
            string_length(123)

    def test_long_string(self):
        self.assertEqual(string_length("abcdefghijklmnopqrstuvwxyz"), 26)

    def test_string_with_punctuation(self):
        self.assertEqual(string_length("hello, world!"), 13)
