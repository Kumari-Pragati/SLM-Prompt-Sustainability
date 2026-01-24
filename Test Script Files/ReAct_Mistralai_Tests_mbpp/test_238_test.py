import unittest
from mbpp_238_code import number_of_substrings

class TestNumberOfSubstrings(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(number_of_substrings(""), 0)

    def test_single_character_string(self):
        for char in "abcdefghijklmnopqrstuvwxyz":
            self.assertEqual(number_of_substrings(char), 1)

    def test_short_strings(self):
        for length in range(2, 10):
            for word in ("a" * length for _ in range(length)):
                self.assertEqual(number_of_substrings(word), length * (length + 1) // 2)

    def test_long_strings(self):
        long_string = "a" * 100
        self.assertEqual(number_of_substrings(long_string), 5050)

    def test_negative_string(self):
        with self.assertRaises(ValueError):
            number_of_substrings("-123")

    def test_string_with_non_alphanumeric_characters(self):
        with self.assertRaises(ValueError):
            number_of_substrings("ab!c1d_e2f")
