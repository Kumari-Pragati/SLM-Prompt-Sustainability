import unittest
from741_code import all_Characters_Same

class TestAllCharactersSame(unittest.TestCase):
    def test_empty_string(self):
        self.assertTrue(all_Characters_Same(""))

    def test_single_character(self):
        for char in "abcdefghijklmnopqrstuvwxyz":
            self.assertTrue(all_Characters_Same(char))

    def test_multiple_same_characters(self):
        for char in "abcdefghijklmnopqrstuvwxyz":
            self.assertTrue(all_Characters_Same(char * 10))

    def test_different_characters(self):
        for char1 in "abcdefghijklmnopqrstuvwxyz":
            for char2 in "abcdefghijklmnopqrstuvwxyz":
                if char1 != char2:
                    self.assertFalse(all_Characters_Same(char1 + char2))

    def test_mixed_case(self):
        for lower in "abcdefghijklmnopqrstuvwxyz":
            for upper in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                self.assertFalse(all_Characters_Same(lower + upper))

    def test_empty_list(self):
        self.assertFalse(all_Characters_Same([]))
