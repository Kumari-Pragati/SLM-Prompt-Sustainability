import unittest
from mbpp_741_code import all_Characters_Same

class TestAllCharactersSame(unittest.TestCase):

    def test_all_same_characters_in_string(self):
        self.assertTrue(all_Characters_Same('aaa'))
        self.assertTrue(all_Characters_Same('bbbb'))
        self.assertTrue(all_Characters_Same('cccc'))

    def test_different_characters_in_string(self):
        self.assertFalse(all_Characters_Same('ab'))
        self.assertFalse(all_Characters_Same('abc'))
        self.assertFalse(all_Characters_Same('abcd'))

    def test_empty_string(self):
        self.assertTrue(all_Characters_Same(''))

    def test_single_character_string(self):
        self.assertTrue(all_Characters_Same('a'))
        self.assertTrue(all_Characters_Same('b'))
        self.assertTrue(all_Characters_Same('c'))

    def test_string_with_spaces(self):
        self.assertFalse(all_Characters_Same('a b'))
        self.assertFalse(all_Characters_Same('a   b'))

    def test_string_with_special_characters(self):
        self.assertFalse(all_Characters_Same('a@a'))
        self.assertFalse(all_Characters_Same('a#a'))
        self.assertFalse(all_Characters_Same('a$a'))
