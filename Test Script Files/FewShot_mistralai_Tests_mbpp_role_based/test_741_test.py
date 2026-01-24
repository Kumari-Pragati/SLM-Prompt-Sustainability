import unittest
from mbpp_741_code import all_Characters_Same

class TestAllCharactersSame(unittest.TestCase):
    def test_single_character(self):
        self.assertTrue(all_Characters_Same("a"))

    def test_two_characters(self):
        self.assertTrue(all_Characters_Same("aa"))

    def test_multiple_characters(self):
        self.assertTrue(all_Characters_Same("aaaa"))

    def test_empty_string(self):
        self.assertTrue(all_Characters_Same(""))

    def test_two_different_characters(self):
        self.assertFalse(all_Characters_Same("ab"))

    def test_two_different_characters_at_start(self):
        self.assertFalse(all_Characters_Same("Ba"))

    def test_two_different_characters_at_end(self):
        self.assertFalse(all_Characters_Same("abA"))
