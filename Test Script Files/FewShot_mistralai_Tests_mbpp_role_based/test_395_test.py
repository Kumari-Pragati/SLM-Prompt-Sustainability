import unittest
from mbpp_395_code import first_non_repeating_character

class TestFirstNonRepeatingCharacter(unittest.TestCase):
    def test_single_character(self):
        self.assertEqual(first_non_repeating_character('a'), 'a')

    def test_empty_string(self):
        self.assertIsNone(first_non_repeating_character(''))

    def test_repeating_characters(self):
        self.assertIsNone(first_non_repeating_character('aa'))

    def test_alternating_characters(self):
        self.assertEqual(first_non_repeating_character('abab'), 'b')

    def test_long_string(self):
        self.assertEqual(first_non_repeating_character('abcdefghijklmnopqrstuvwxyz'), 'a')

    def test_uppercase_letters(self):
        self.assertEqual(first_non_repeating_character('ABC'), 'A')

    def test_numbers(self):
        self.assertIsNone(first_non_repeating_character('123'))

    def test_special_characters(self):
        self.assertIsNone(first_non_repeating_character('!@#$%^&*()'))
