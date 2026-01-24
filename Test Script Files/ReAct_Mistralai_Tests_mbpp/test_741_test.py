import unittest
from mbpp_741_code import all_Characters_Same

class TestAllCharactersSame(unittest.TestCase):

    def test_empty_string(self):
        """Check if empty string returns True"""
        self.assertTrue(all_Characters_Same(""))

    def test_single_character_string(self):
        """Check if single character string returns True"""
        for char in "abcdefghijklmnopqrstuvwxyz":
            self.assertTrue(all_Characters_Same(char))

    def test_multiple_same_characters_string(self):
        """Check if multiple same characters string returns True"""
        for char in "abcdefghijklmnopqrstuvwxyz":
            self.assertTrue(all_Characters_Same(char * 10))

    def test_different_characters_string(self):
        """Check if different characters string returns False"""
        for char1 in "abcdefghijklmnopqrstuvwxyz":
            for char2 in "abcdefghijklmnopqrstuvwxyz":
                if char1 != char2:
                    self.assertFalse(all_Characters_Same(char1 + char2))

    def test_special_characters_string(self):
        """Check if string with special characters returns False"""
        self.assertFalse(all_Characters_Same("!@#$%^&*()_+-="))

    def test_numbers_string(self):
        """Check if string with numbers returns False"""
        self.assertFalse(all_Characters_Same("1234567890"))
