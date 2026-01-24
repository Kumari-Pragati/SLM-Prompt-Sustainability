import unittest
from mbpp_395_code import first_non_repeating_character

class TestFirstNonRepeatingCharacter(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(first_non_repeating_character("abcdef"), 'a')

    def test_edge_case_empty_string(self):
        self.assertIsNone(first_non_repeating_character(""))

    def test_edge_case_single_character(self):
        self.assertEqual(first_non_repeating_character("a"), 'a')

    def test_edge_case_all_duplicates(self):
        self.assertIsNone(first_non_repeating_character("aaaa"))

    def test_edge_case_all_unique(self):
        self.assertEqual(first_non_repeating_character("abcdef"), 'a')

    def test_edge_case_all_unique_and_empty(self):
        self.assertIsNone(first_non_repeating_character(""))

    def test_edge_case_all_unique_and_single_character(self):
        self.assertEqual(first_non_repeating_character("a"), 'a')

    def test_edge_case_all_unique_and_duplicates(self):
        self.assertEqual(first_non_repeating_character("abcabc"), 'a')

    def test_edge_case_all_unique_and_duplicates_and_empty(self):
        self.assertIsNone(first_non_repeating_character(""))

    def test_edge_case_all_unique_and_duplicates_and_single_character(self):
        self.assertEqual(first_non_repeating_character("aabc"), 'a')
