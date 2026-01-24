import unittest
from mbpp_741_code import all_Characters_Same

class TestAllCharactersSame(unittest.TestCase):

    def test_same_characters(self):
        self.assertTrue(all_Characters_Same('aaa'))
        self.assertTrue(all_Characters_Same('bbbb'))
        self.assertTrue(all_Characters_Same('ccccc'))

    def test_different_characters(self):
        self.assertFalse(all_Characters_Same('aab'))
        self.assertFalse(all_Characters_Same('abc'))
        self.assertFalse(all_Characters_Same('abcd'))

    def test_empty_string(self):
        self.assertTrue(all_Characters_Same(''))

    def test_single_character(self):
        self.assertTrue(all_Characters_Same('a'))
        self.assertTrue(all_Characters_Same('b'))
        self.assertTrue(all_Characters_Same('c'))
