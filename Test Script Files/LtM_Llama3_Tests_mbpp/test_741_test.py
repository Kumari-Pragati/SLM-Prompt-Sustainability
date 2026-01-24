import unittest
from mbpp_741_code import all_Characters_Same

class TestAll_Characters_Same(unittest.TestCase):
    def test_simple_valid_input(self):
        self.assertTrue(all_Characters_Same("aaaaaa"))

    def test_empty_input(self):
        self.assertFalse(all_Characters_Same(""))

    def test_single_character_input(self):
        self.assertTrue(all_Characters_Same("a"))

    def test_all_characters_same(self):
        self.assertTrue(all_Characters_Same("abcabcabc"))

    def test_all_characters_not_same(self):
        self.assertFalse(all_Characters_Same("ababab"))

    def test_long_string_input(self):
        self.assertTrue(all_Characters_Same("abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"))

    def test_mixed_case_input(self):
        self.assertTrue(all_Characters_Same("aAaAaA"))

    def test_punctuation_input(self):
        self.assertTrue(all_Characters_Same(".,.,.,.,."))

    def test_numbers_input(self):
        self.assertTrue(all_Characters_Same("1234567890"))

    def test_spaces_input(self):
        self.assertTrue(all_Characters_Same("   "))
