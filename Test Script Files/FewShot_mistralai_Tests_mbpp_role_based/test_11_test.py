import unittest
from mbpp_11_code import remove_Occ

class TestRemoveOcc(unittest.TestCase):
    def test_remove_single_occurrence(self):
        self.assertEqual(remove_Occ("abcabc", "a"), "bcbc")

    def test_remove_multiple_occurrences(self):
        self.assertEqual(remove_Occ("aaabbbccc", "a"), "bbbccc")

    def test_empty_string(self):
        self.assertEqual(remove_Occ("", "a"), "")

    def test_single_character_string(self):
        self.assertEqual(remove_Occ("a", "a"), "")

    def test_string_with_only_one_character(self):
        self.assertEqual(remove_Occ("a", "b"), "a")

    def test_string_with_no_occurrences(self):
        self.assertEqual(remove_Occ("abc", "x"), "abc")
