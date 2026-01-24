import unittest
from mbpp_238_code import number_of_substrings

class TestNumberOfSubstrings(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(number_of_substrings(""), 0)

    def test_single_character_string(self):
        self.assertEqual(number_of_substrings("a"), 1)

    def test_multiple_character_string(self):
        self.assertEqual(number_of_substrings("abc"), 3)

    def test_long_string(self):
        self.assertEqual(number_of_substrings("abcdefghijklmnopqrstuvwxyz"), 78)

    def test_non_string_input(self):
        with self.assertRaises(TypeError):
            number_of_substrings(123)
