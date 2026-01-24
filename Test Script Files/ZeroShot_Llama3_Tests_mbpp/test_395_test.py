import unittest
from mbpp_395_code import first_non_repeating_character

class TestFirstNonRepeatingCharacter(unittest.TestCase):

    def test_empty_string(self):
        self.assertIsNone(first_non_repeating_character(""))

    def test_single_character(self):
        self.assertEqual(first_non_repeating_character("a"), 'a')

    def test_multiple_characters(self):
        self.assertEqual(first_non_repeating_character("aabbc"), 'c')

    def test_no_non_repeating_character(self):
        self.assertIsNone(first_non_repeating_character("aaaabbbcc"))

    def test_non_repeating_character_at_start(self):
        self.assertEqual(first_non_repeating_character("abcde"), 'a')

    def test_non_repeating_character_at_end(self):
        self.assertEqual(first_non_repeating_character("edcba"), 'a')

    def test_non_repeating_character_in_middle(self):
        self.assertEqual(first_non_repeating_character("abacde"), 'c')

    def test_non_repeating_character_at_start_and_end(self):
        self.assertEqual(first_non_repeating_character("abcdeabc"), 'a')

    def test_non_repeating_character_at_start_and_end_and_middle(self):
        self.assertEqual(first_non_repeating_character("abcdeabcde"), 'a')
