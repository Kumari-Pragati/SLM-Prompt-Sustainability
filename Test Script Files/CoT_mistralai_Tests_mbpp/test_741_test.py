import unittest
from741_code import all_Characters_Same

class TestAllCharactersSame(unittest.TestCase):
    def test_empty_string(self):
        self.assertTrue(all_Characters_Same(""))

    def test_single_character_string(self):
        for char in "abcdefghijklmnopqrstuvwxyz":
            self.assertTrue(all_Characters_Same(char))

    def test_multiple_characters_same(self):
        for char in "aaaaaaa":
            self.assertTrue(all_Characters_Same(char))

    def test_multiple_characters_different(self):
        for char1 in "abcdefghijklmnopqrstuvwxyz"[:10]:
            for char2 in "abcdefghijklmnopqrstuvwxyz"[10:]:
                self.assertFalse(all_Characters_Same(char1 + char2))

    def test_string_with_non_alphabet_characters(self):
        for char in "!@#$%^&*()_+-=[]{};':\"\\|,.<>/? ":
            self.assertFalse(all_Characters_Same(char))

        for char1 in "abcdefghijklmnopqrstuvwxyz"[:10]:
            self.assertFalse(all_Characters_Same(char1 + "!"))
