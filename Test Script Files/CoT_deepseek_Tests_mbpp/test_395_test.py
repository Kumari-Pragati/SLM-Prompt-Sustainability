import unittest
from mbpp_395_code import first_non_repeating_character

class TestFirstNonRepeatingCharacter(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(first_non_repeating_character('aabbc'), 'c')

    def test_single_character(self):
        self.assertEqual(first_non_repeating_character('a'), 'a')

    def test_no_repeating_characters(self):
        self.assertEqual(first_non_repeating_character('abcd'), None)

    def test_empty_string(self):
        self.assertEqual(first_non_repeating_character(''), None)

    def test_repeated_characters(self):
        self.assertEqual(first_non_repeating_character('aabbcc'), None)

    def test_case_sensitivity(self):
        self.assertEqual(first_non_repeating_character('AaBb'), 'B')

    def test_numeric_characters(self):
        self.assertEqual(first_non_repeating_character('123123'), None)

    def test_special_characters(self):
        self.assertEqual(first_non_repeating_character('!@#!@#'), '#')
