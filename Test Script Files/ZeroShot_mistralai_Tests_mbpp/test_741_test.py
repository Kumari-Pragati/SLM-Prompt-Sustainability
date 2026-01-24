import unittest
from741_code import all_Characters_Same

class TestAllCharactersSame(unittest.TestCase):

    def test_empty_string(self):
        self.assertTrue(all_Characters_Same(""))

    def test_single_character_string(self):
        for char in "abcdefghijklmnopqrstuvwxyz":
            self.assertTrue(all_Characters_Same(char))

    def test_multiple_characters_same_string(self):
        self.assertTrue(all_Characters_Same("aaaaaa"))

    def test_multiple_characters_different_string(self):
        self.assertFalse(all_Characters_Same("abcdabcd"))

    def test_mixed_case_string(self):
        self.assertFalse(all_Characters_Same("AbCdEfGhIjKlMnOpQrStUvWxYz"))

    def test_special_characters_string(self):
        self.assertFalse(all_Characters_Same("!@#$%^&*()_+-=[]{}|;:'\",.<>/?"))

    def test_numbers_string(self):
        self.assertFalse(all_Characters_Same("1234567890"))
