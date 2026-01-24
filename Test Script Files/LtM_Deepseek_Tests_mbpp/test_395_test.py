import unittest
from mbpp_395_code import first_non_repeating_character

class TestFirstNonRepeatingCharacter(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(first_non_repeating_character('aabbc'), 'c')
        self.assertEqual(first_non_repeating_character('abc'), 'a')
        self.assertEqual(first_non_repeating_character('aabbcc'), None)

    def test_edge_conditions(self):
        self.assertEqual(first_non_repeating_character(''), None)
        self.assertEqual(first_non_repeating_character('a'), 'a')
        self.assertEqual(first_non_repeating_character('aa'), None)

    def test_complex_cases(self):
        self.assertEqual(first_non_repeating_character('aabbccddeeffg'), 'd')
        self.assertEqual(first_non_repeating_character('aabbccddeeffgg'), None)
        self.assertEqual(first_non_repeating_character('abcdefgabcdefg'), None)
