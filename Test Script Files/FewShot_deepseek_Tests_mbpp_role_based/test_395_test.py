import unittest
from mbpp_395_code import first_non_repeating_character

class TestFirstNonRepeatingCharacter(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(first_non_repeating_character('aabbc'), 'c')

    def test_edge_case_single_character(self):
        self.assertEqual(first_non_repeating_character('a'), 'a')

    def test_boundary_case_empty_string(self):
        self.assertIsNone(first_non_repeating_character(''))

    def test_boundary_case_all_repeating_characters(self):
        self.assertIsNone(first_non_repeating_character('aaaaa'))

    def test_typical_use_case_with_numbers(self):
        self.assertEqual(first_non_repeating_character('11223344556677889900'), '0')

    def test_typical_use_case_with_mixed_case(self):
        self.assertEqual(first_non_repeating_character('AaBbCc'), 'A')

    def test_typical_use_case_with_special_characters(self):
        self.assertEqual(first_non_repeating_character('!@#$%^&*()'), '!')
