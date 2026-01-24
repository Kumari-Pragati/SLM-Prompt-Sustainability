import unittest
from mbpp_741_code import all_Characters_Same

class TestAllCharactersSame(unittest.TestCase):
    def test_all_same_characters(self):
        self.assertTrue(all_Characters_Same('aaa'))

    def test_different_characters(self):
        self.assertFalse(all_Characters_Same('aab'))

    def test_empty_string(self):
        self.assertTrue(all_Characters_Same(''))

    def test_single_character(self):
        self.assertTrue(all_Characters_Same('a'))

    def test_whitespace_string(self):
        self.assertFalse(all_Characters_Same('a b'))

    def test_numeric_string(self):
        self.assertTrue(all_Characters_Same('111'))

    def test_mixed_case_string(self):
        self.assertFalse(all_Characters_Same('Aa'))
