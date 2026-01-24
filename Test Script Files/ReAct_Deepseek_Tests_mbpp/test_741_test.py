import unittest
from mbpp_741_code import all_Characters_Same

class TestAllCharactersSame(unittest.TestCase):

    def test_all_same_characters_typical(self):
        self.assertTrue(all_Characters_Same('aaaaa'))

    def test_all_same_characters_empty(self):
        self.assertTrue(all_Characters_Same(''))

    def test_all_different_characters(self):
        self.assertFalse(all_Characters_Same('abcde'))

    def test_all_same_characters_single(self):
        self.assertTrue(all_Characters_Same('a'))

    def test_all_same_characters_with_spaces(self):
        self.assertFalse(all_Characters_Same('a b c d e'))

    def test_all_same_characters_with_special_characters(self):
        self.assertFalse(all_Characters_Same('a@b@c@d@e'))

    def test_all_same_characters_with_numbers(self):
        self.assertFalse(all_Characters_Same('12345'))
