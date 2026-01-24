import unittest
from mbpp_395_code import first_non_repeating_character

class TestFirstNonRepeatingCharacter(unittest.TestCase):
    def test_typical_input(self):
        self.assertEqual(first_non_repeating_character("aabbc"), 'b')

    def test_edge_case_empty_string(self):
        self.assertIsNone(first_non_repeating_character(''))

    def test_edge_case_single_character_string(self):
        self.assertEqual(first_non_repeating_character('a'), 'a')

    def test_edge_case_all_duplicates(self):
        self.assertIsNone(first_non_repeating_character("aaaaaa"))

    def test_edge_case_all_unique(self):
        self.assertEqual(first_non_repeating_character("abcdef"), 'a')

    def test_edge_case_all_unique_and_order_matters(self):
        self.assertEqual(first_non_repeating_character("abcdef"), 'a')

    def test_invalid_input_non_string(self):
        with self.assertRaises(TypeError):
            first_non_repeating_character(123)

    def test_invalid_input_non_string_with_spaces(self):
        with self.assertRaises(TypeError):
            first_non_repeating_character("123 spaces")

    def test_edge_case_multiple_non_repeating_characters(self):
        self.assertEqual(first_non_repeating_character("abcabc"), 'a')

    def test_edge_case_no_non_repeating_characters(self):
        self.assertIsNone(first_non_repeating_character("aaabbb"))
