import unittest
from mbpp_741_code import all_Characters_Same

class TestAllCharactersSame(unittest.TestCase):

    def test_all_characters_same_typical(self):
        self.assertTrue(all_Characters_Same('aaa'))
        self.assertTrue(all_Characters_Same('111'))
        self.assertTrue(all_Characters_Same(''))

    def test_all_characters_same_edge(self):
        self.assertTrue(all_Characters_Same('a'))
        self.assertTrue(all_Characters_Same('1'))
        self.assertTrue(all_Characters_Same(' '))

    def test_all_characters_same_complex(self):
        self.assertFalse(all_Characters_Same('ab'))
        self.assertFalse(all_Characters_Same('a1'))
        self.assertFalse(all_Characters_Same('abc'))
