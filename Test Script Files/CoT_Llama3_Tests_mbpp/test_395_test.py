import unittest
from mbpp_395_code import first_non_repeating_character

class TestFirstNonRepeatingCharacter(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(first_non_repeating_character("aabbcc"), 'c')

    def test_edge_case(self):
        self.assertEqual(first_non_repeating_character("abcabc"), 'b')

    def test_multiple_non_repeating_characters(self):
        self.assertEqual(first_non_repeating_character("abcdef"), 'a')

    def test_no_non_repeating_characters(self):
        self.assertIsNone(first_non_repeating_character("aaabbbcc"))

    def test_empty_string(self):
        self.assertIsNone(first_non_repeating_character(""))

    def test_single_character(self):
        self.assertEqual(first_non_repeating_character("a"), 'a')

    def test_all_repeating_characters(self):
        self.assertIsNone(first_non_repeating_character("aaaaaa"))
