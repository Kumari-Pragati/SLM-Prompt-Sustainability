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

    def test_string_with_duplicates(self):
        self.assertEqual(number_of_substrings("aabbcc"), 6)

    def test_string_with_duplicates_and_spaces(self):
        self.assertEqual(number_of_substrings("aabbcc  "), 6)

    def test_string_with_duplicates_and_spaces_and_punctuation(self):
        self.assertEqual(number_of_substrings("aabbcc.,!"), 6)

    def test_string_with_duplicates_and_spaces_and_punctuation_and_numbers(self):
        self.assertEqual(number_of_substrings("aabbcc.,! 123"), 6)

    def test_string_with_duplicates_and_spaces_and_punctuation_and_numbers_and_special_chars(self):
        self.assertEqual(number_of_substrings("aabbcc.,! 123 @ # $"), 6)
