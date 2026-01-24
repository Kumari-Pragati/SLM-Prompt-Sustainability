import unittest
from mbpp_238_code import number_of_substrings

class TestNumberOfSubstrings(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(number_of_substrings(""), 0)

    def test_single_character_string(self):
        self.assertEqual(number_of_substrings("a"), 1)

    def test_short_string(self):
        self.assertEqual(number_of_substrings("abc"), 3)

    def test_long_string(self):
        self.assertEqual(number_of_substrings("abcdefghijklmnopqrstuvwxyz"), 78)

    def test_string_with_repeated_characters(self):
        self.assertEqual(number_of_substrings("aaabbbccc"), 21)

    def test_string_with_spaces(self):
        self.assertEqual(number_of_substrings("a b c"), 3)

    def test_string_with_punctuation(self):
        self.assertEqual(number_of_substrings("Hello, World!"), 6)

    def test_string_with_digits(self):
        self.assertEqual(number_of_substrings("1234567890"), 45)

    def test_string_with_special_characters(self):
        self.assertEqual(number_of_substrings("Hello, World!@#"), 6)
