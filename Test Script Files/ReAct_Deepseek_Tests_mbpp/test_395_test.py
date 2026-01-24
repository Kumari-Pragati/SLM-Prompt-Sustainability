import unittest
from mbpp_395_code import first_non_repeating_character

class TestFirstNonRepeatingCharacter(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(first_non_repeating_character('aabbc'), 'c')
        self.assertEqual(first_non_repeating_character('abc'), 'a')
        self.assertEqual(first_non_repeating_character('aabbcc'), None)

    def test_edge_cases(self):
        self.assertEqual(first_non_repeating_character(''), None)
        self.assertEqual(first_non_repeating_character('a'), 'a')
        self.assertEqual(first_non_repeating_character('aaa'), None)

    def test_explicitly_handled_error_cases(self):
        self.assertIsNone(first_non_repeating_character(None))
        self.assertIsNone(first_non_repeating_character(123))
