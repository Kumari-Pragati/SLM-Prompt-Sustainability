import unittest
from mbpp_395_code import first_non_repeating_character

class TestFirstNonRepeatingCharacter(unittest.TestCase):
    def test_simple_valid_input(self):
        self.assertEqual(first_non_repeating_character("a"), 'a')

    def test_multiple_non_repeating_characters(self):
        self.assertEqual(first_non_repeating_character("abc"), 'a')

    def test_multiple_repeating_characters(self):
        self.assertEqual(first_non_repeating_character("aaabbb"), None)

    def test_empty_string(self):
        self.assertEqual(first_non_repeating_character(""), None)

    def test_single_character(self):
        self.assertEqual(first_non_repeating_character("a"), 'a')

    def test_no_non_repeating_characters(self):
        self.assertEqual(first_non_repeating_character("aaa"), None)

    def test_long_string(self):
        self.assertEqual(first_non_repeating_character("abcdefghijklmnopqrstuvwxyz"), 'a')
