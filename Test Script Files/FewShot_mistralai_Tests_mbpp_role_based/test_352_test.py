import unittest
from mbpp_352_code import unique_Characters

class TestUniqueCharacters(unittest.TestCase):
    def test_unique_characters_in_string(self):
        self.assertTrue(unique_Characters("abcdefghijklmnopqrstuvwxyz"))

    def test_unique_characters_in_mixed_case_string(self):
        self.assertTrue(unique_Characters("AbCdEfGhIjKlMnOpQrStUvWxYz"))

    def test_unique_characters_in_empty_string(self):
        self.assertTrue(unique_Characters(""))

    def test_unique_characters_in_single_character_string(self):
        self.assertTrue(unique_Characters("a"))

    def test_unique_characters_in_duplicate_characters_string(self):
        self.assertFalse(unique_Characters("aa"))

    def test_unique_characters_in_string_with_special_characters(self):
        self.assertTrue(unique_Characters("abc!def456"))

    def test_unique_characters_in_string_with_whitespace(self):
        self.assertTrue(unique_Characters("abc def ghi"))
