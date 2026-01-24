import unittest
from mbpp_395_code import first_non_repeating_character

class TestFirstNonRepeatingCharacter(unittest.TestCase):

    def test_empty_string(self):
        self.assertIsNone(first_non_repeating_character(''))

    def test_single_character(self):
        self.assertEqual(first_non_repeating_character('a'), 'a')

    def test_repeated_characters(self):
        self.assertIsNone(first_non_repeating_character('aa'))

    def test_multiple_non_repeated_characters(self):
        self.assertEqual(first_non_repeating_character('abc'), 'a')

    def test_multiple_repeated_characters(self):
        self.assertIsNone(first_non_repeating_character('aaa'))

    def test_long_string(self):
        self.assertEqual(first_non_repeating_character('abcdefghijklmnopqrstuvwxyz'), 'a')

    def test_string_with_repeated_and_non_repeated_characters(self):
        self.assertEqual(first_non_repeating_character('ababc'), 'b')

    def test_string_with_only_digits(self):
        self.assertEqual(first_non_repeating_character('12345'), '1')

    def test_string_with_only_special_characters(self):
        self.assertEqual(first_non_repeating_character('!@#$%^&*()'), '!')

    def test_string_with_only_uppercase_letters(self):
        self.assertEqual(first_non_repeating_character('ABCDEFGHIJKLMNOPQRSTUVWXYZ'), 'A')

    def test_string_with_only_lowercase_letters(self):
        self.assertEqual(first_non_repeating_character('abcdefghijklmnopqrstuvwxyz'), 'a')

    def test_string_with_special_and_letters(self):
        self.assertEqual(first_non_repeating_character('A!B@C$'), 'A')
