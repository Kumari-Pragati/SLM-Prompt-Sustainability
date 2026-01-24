import unittest
from mbpp_352_code import unique_Characters

class TestUniqueCharacters(unittest.TestCase):
    def test_typical_input(self):
        self.assertTrue(unique_Characters("abcdefg"))

    def test_edge_case_empty_string(self):
        self.assertTrue(unique_Characters(""))

    def test_edge_case_single_character(self):
        self.assertTrue(unique_Characters("a"))

    def test_edge_case_all_duplicates(self):
        self.assertFalse(unique_Characters("aaa"))

    def test_edge_case_all_unique(self):
        self.assertTrue(unique_Characters("abcdefg"))

    def test_edge_case_all_duplicates_reversed(self):
        self.assertFalse(unique_Characters("aaa"))

    def test_edge_case_all_unique_reversed(self):
        self.assertTrue(unique_Characters("gfedcba"))

    def test_edge_case_all_duplicates_and_unique(self):
        self.assertFalse(unique_Characters("aabbcc"))

    def test_edge_case_all_unique_and_duplicates(self):
        self.assertFalse(unique_Characters("aabbcc"))

    def test_edge_case_empty_string_with_duplicates(self):
        self.assertTrue(unique_Characters(""))

    def test_edge_case_empty_string_with_unique(self):
        self.assertTrue(unique_Characters(""))

    def test_edge_case_single_character_with_duplicates(self):
        self.assertFalse(unique_Characters("aa"))

    def test_edge_case_single_character_with_unique(self):
        self.assertTrue(unique_Characters("a"))

    def test_edge_case_all_duplicates_with_duplicates(self):
        self.assertFalse(unique_Characters("aaaa"))

    def test_edge_case_all_unique_with_duplicates(self):
        self.assertFalse(unique_Characters("abcdefg"))

    def test_edge_case_all_duplicates_with_unique(self):
        self.assertFalse(unique_Characters("aabbcc"))

    def test_edge_case_all_unique_with_unique(self):
        self.assertTrue(unique_Characters("abcdefg"))

    def test_edge_case_empty_string_with_duplicates_and_unique(self):
        self.assertTrue(unique_Characters(""))

    def test_edge_case_empty_string_with_unique_and_duplicates(self):
        self.assertTrue(unique_Characters(""))

    def test_edge_case_single_character_with_duplicates_and_unique(self):
        self.assertFalse(unique_Characters("aa"))

    def test_edge_case_single_character_with_unique_and_duplicates(self):
        self.assertFalse(unique_Characters("a"))

    def test_edge_case_all_duplicates_with_duplicates_and_unique(self):
        self.assertFalse(unique_Characters("aaaa"))

    def test_edge_case_all_unique_with_duplicates_and_unique(self):
        self.assertFalse(unique_Characters("abcdefg"))
