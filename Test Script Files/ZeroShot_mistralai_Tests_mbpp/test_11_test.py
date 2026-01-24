import unittest
from mbpp_11_code import remove_Occ

class TestRemoveOcc(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(remove_Occ("", "a"), "")

    def test_single_character(self):
        self.assertEqual(remove_Occ("a", "a"), "")
        self.assertEqual(remove_Occ("A", "a"), "A")

    def test_multiple_characters(self):
        self.assertEqual(remove_Occ("aaa", "a"), "")
        self.assertEqual(remove_Occ("AAA", "a"), "AAA")
        self.assertEqual(remove_Occ("aaBbCc", "a"), "BbCc")
        self.assertEqual(remove_Occ("aaBbCc", "b"), "aaCc")
        self.assertEqual(remove_Occ("aaBbCc", "c"), "aaBb")

    def test_multiple_occurrences(self):
        self.assertEqual(remove_Occ("aaa", "a"), "")
        self.assertEqual(remove_Occ("aaa", "b"), "aaa")

    def test_single_character_at_start_and_end(self):
        self.assertEqual(remove_Occ("aa", "a"), "")
        self.assertEqual(remove_Occ("aa", "b"), "aa")
        self.assertEqual(remove_Occ("aa", "a"), "")

    def test_string_with_only_one_character(self):
        self.assertEqual(remove_Occ("a", "a"), "")
        self.assertEqual(remove_Occ("A", "a"), "A")
