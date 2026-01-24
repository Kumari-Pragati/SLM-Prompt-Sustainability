import unittest
from mbpp_741_code import all_Characters_Same

class TestAll_Characters_Same(unittest.TestCase):

    def test_all_characters_same(self):
        self.assertTrue(all_Characters_Same("aaaaaa"))
    def test_all_characters_not_same(self):
        self.assertFalse(all_Characters_Same("abcde"))
    def test_single_character(self):
        self.assertTrue(all_Characters_Same("a"))
    def test_empty_string(self):
        self.assertTrue(all_Characters_Same(""))
    def test_single_character_string(self):
        self.assertTrue(all_Characters_Same("a"))
    def test_all_characters_same_with_spaces(self):
        self.assertTrue(all_Characters_Same("aaaaaa "))
    def test_all_characters_not_same_with_spaces(self):
        self.assertFalse(all_Characters_Same("a b c d e"))
