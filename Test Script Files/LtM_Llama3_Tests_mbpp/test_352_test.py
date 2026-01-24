import unittest
from mbpp_352_code import unique_Characters

class TestUniqueCharacters(unittest.TestCase):
    def test_empty_string(self):
        self.assertTrue(unique_Characters(''))

    def test_single_character_string(self):
        self.assertTrue(unique_Characters('a'))

    def test_all_unique_characters(self):
        self.assertTrue(unique_Characters('abcde'))

    def test_all_unique_characters_with_spaces(self):
        self.assertTrue(unique_Characters('a b c d e'))

    def test_duplicates(self):
        self.assertFalse(unique_Characters('aabbcc'))

    def test_duplicates_with_spaces(self):
        self.assertFalse(unique_Characters('a b b c c'))

    def test_duplicates_at_end(self):
        self.assertFalse(unique_Characters('abcba'))

    def test_duplicates_at_start(self):
        self.assertFalse(unique_Characters('aabbcc'))

    def test_duplicates_at_start_and_end(self):
        self.assertFalse(unique_Characters('aabbccba'))

    def test_duplicates_in_middle(self):
        self.assertFalse(unique_Characters('aabbccba'))
