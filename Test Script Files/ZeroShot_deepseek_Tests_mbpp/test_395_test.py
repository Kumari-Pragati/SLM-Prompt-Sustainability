import unittest
from mbpp_395_code import first_non_repeating_character

class TestFirstNonRepeatingCharacter(unittest.TestCase):

    def test_empty_string(self):
        self.assertIsNone(first_non_repeating_character(''))

    def test_single_character(self):
        self.assertEqual(first_non_repeating_character('a'), 'a')

    def test_all_repeating(self):
        self.assertIsNone(first_non_repeating_character('aaa'))

    def test_all_unique(self):
        self.assertEqual(first_non_repeating_character('abc'), 'a')

    def test_mixed(self):
        self.assertEqual(first_non_repeating_character('abca'), 'b')
        self.assertEqual(first_non_repeating_character('abac'), 'c')
