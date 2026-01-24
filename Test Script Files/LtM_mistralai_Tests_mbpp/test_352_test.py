import unittest
from mbpp_352_code import unique_Characters

class TestUniqueCharacters(unittest.TestCase):

    def test_simple_unique_string(self):
        self.assertTrue(unique_Characters("abc"))

    def test_empty_string(self):
        self.assertTrue(unique_Characters(""))

    def test_single_character_string(self):
        self.assertTrue(unique_Characters("a"))
        self.assertFalse(unique_Characters("aa"))

    def test_duplicate_characters_in_middle(self):
        self.assertFalse(unique_Characters("abba"))

    def test_duplicate_characters_at_start_and_end(self):
        self.assertFalse(unique_Characters("aaa"))

    def test_duplicate_characters_in_middle_and_end(self):
        self.assertFalse(unique_Characters("abbaa"))

    def test_duplicate_characters_in_all_positions(self):
        self.assertFalse(unique_Characters("aaabbb"))
