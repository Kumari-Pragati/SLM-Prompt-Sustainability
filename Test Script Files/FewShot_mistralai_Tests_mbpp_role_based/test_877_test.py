import unittest
from mbpp_877_code import sort_String

class TestSortString(unittest.TestCase):
    def test_sorted_string(self):
        self.assertEqual(sort_String("abcdefghijklmnopqrstuvwxyz"), "abcdefghijklmnopqrstuvwxyz")

    def test_mixed_case_string(self):
        self.assertEqual(sort_String("ABCDEFGHIJKLMNOPQRSTUVWXYZ"), "ABCDEFGHIJKLMNOPQRSTUVWXYZ")

    def test_empty_string(self):
        self.assertEqual(sort_String(""), "")

    def test_single_character_string(self):
        for char in "!@#$%^&*()_+-=[]{};':\"|,.<>/? ":
            self.assertEqual(sort_String(char), char)

    def test_reversed_string(self):
        self.assertEqual(sort_String("zyxwvutsrqponmlkjihgfedcba"), "abcdefghijklmnopqrstuvwxyz")

    def test_duplicate_characters(self):
        self.assertEqual(sort_String("aaabbbccc"), "aaabbbccc")
