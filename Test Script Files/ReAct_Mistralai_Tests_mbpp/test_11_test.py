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
        self.assertEqual(remove_Occ("aaZ", "a"), "Z")
        self.assertEqual(remove_Occ("Zaa", "a"), "Z")

    def test_long_string(self):
        long_string = "a" * 100
        self.assertEqual(remove_Occ(long_string, "a"), "")

    def test_single_character_at_start(self):
        self.assertEqual(remove_Occ("aabb", "a"), "b")
        self.assertEqual(remove_Occ("Aabb", "a"), "Abb")

    def test_single_character_at_end(self):
        self.assertEqual(remove_Occ("abba", "a"), "abb")
        self.assertEqual(remove_Occ("AbBA", "a"), "AbB")

    def test_multiple_characters_at_start(self):
        self.assertEqual(remove_Occ("aaaaabb", "a"), "abb")
        self.assertEqual(remove_Occ("AAAAAbb", "a"), "AAAAbb")

    def test_multiple_characters_at_end(self):
        self.assertEqual(remove_Occ("abbaaa", "a"), "bb")
        self.assertEqual(remove_Occ("ABBAaa", "a"), "ABB")

    def test_non_existent_character(self):
        self.assertEqual(remove_Occ("abc", "x"), "abc")
