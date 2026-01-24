import unittest
from395_code import first_non_repeating_character

class TestFirstNonRepeatingCharacter(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(first_non_repeating_character("abcdefghijklmnopqrstuvwxyz"), "a")
        self.assertEqual(first_non_repeating_character("ABCDEFGHIJKLMNOPQRSTUVWXYZ"), "A")
        self.assertEqual(first_non_repeating_character("1234567890"), "1")
        self.assertEqual(first_non_repeating_character("!@#$%^&*()_+-=[]{}|;:'\",.<>?/"), "!")

    def test_edge_case_empty_string(self):
        self.assertIsNone(first_non_repeating_character(""))

    def test_edge_case_single_character(self):
        self.assertEqual(first_non_repeating_character("a"), "a")

    def test_edge_case_duplicate_characters(self):
        self.assertIsNone(first_non_repeating_character("aa"))
        self.assertIsNone(first_non_repeating_character("abab"))
        self.assertIsNone(first_non_repeating_character("1212"))

    def test_corner_case_all_duplicates(self):
        self.assertIsNone(first_non_repeating_character("aaa"))
        self.assertIsNone(first_non_repeating_character("111"))
        self.assertIsNone(first_non_repeating_character("!@!@"))
