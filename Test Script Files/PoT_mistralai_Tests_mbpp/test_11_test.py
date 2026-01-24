import unittest
from11_code import remove_Occ

class TestRemoveOcc(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(remove_Occ("", "a"), "")

    def test_single_character(self):
        self.assertEqual(remove_Occ("a", "a"), "")
        self.assertEqual(remove_Occ("A", "a"), "A")

    def test_multiple_characters(self):
        self.assertEqual(remove_Occ("aaa", "a"), "")
        self.assertEqual(remove_Occ("AAA", "a"), "AAA")
        self.assertEqual(remove_Occ("aaA", "a"), "aA")

    def test_single_character_at_start_and_end(self):
        self.assertEqual(remove_Occ("aab", "a"), "b")
        self.assertEqual(remove_Occ("Aba", "A"), "ba")

    def test_multiple_characters_at_start_and_end(self):
        self.assertEqual(remove_Occ("aaab", "a"), "b")
        self.assertEqual(remove_Occ("AAAB", "a"), "AAAB")
        self.assertEqual(remove_Occ("aaAB", "a"), "aAB")

    def test_multiple_characters_in_middle(self):
        self.assertEqual(remove_Occ("aaaabb", "a"), "bb")
        self.assertEqual(remove_Occ("AAAABB", "a"), "AAABB")
        self.assertEqual(remove_Occ("aaABB", "a"), "aABB")
