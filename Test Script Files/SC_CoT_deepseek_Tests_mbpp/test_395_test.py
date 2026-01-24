import unittest
from mbpp_395_code import first_non_repeating_character

class TestFirstNonRepeatingCharacter(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(first_non_repeating_character('aabbc'), 'c')

    def test_edge_case_empty_string(self):
        self.assertIsNone(first_non_repeating_character(''))

    def test_edge_case_single_character(self):
        self.assertEqual(first_non_repeating_character('a'), 'a')

    def test_corner_case_all_repeating(self):
        self.assertIsNone(first_non_repeating_character('aabbcc'))

    def test_corner_case_all_non_repeating(self):
        self.assertEqual(first_non_repeating_character('abc'), 'a')

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            first_non_repeating_character(123)
