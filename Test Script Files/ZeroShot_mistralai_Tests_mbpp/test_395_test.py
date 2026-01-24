import unittest
from mbpp_395_code import first_non_repeating_character

class TestFirstNonRepeatingCharacter(unittest.TestCase):

    def test_empty_string(self):
        self.assertIsNone(first_non_repeating_character(''))

    def test_single_character(self):
        self.assertEqual(first_non_repeating_character('a'), 'a')

    def test_single_repeated_character(self):
        self.assertIsNone(first_non_repeating_character('aa'))

    def test_multiple_characters(self):
        self.assertEqual(first_non_repeating_character('abc'), 'a')

    def test_multiple_repeated_characters(self):
        self.assertIsNone(first_non_repeating_character('aaa'))

    def test_multiple_characters_with_repeated(self):
        self.assertEqual(first_non_repeating_character('abcc'), 'c')

    def test_multiple_characters_with_repeated_and_non_repeated(self):
        self.assertEqual(first_non_repeating_character('abac'), 'a')
