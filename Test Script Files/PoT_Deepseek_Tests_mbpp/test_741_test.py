import unittest
from mbpp_741_code import all_Characters_Same

class TestAllCharactersSame(unittest.TestCase):

    def test_typical_cases(self):
        self.assertTrue(all_Characters_Same('aaa'))
        self.assertTrue(all_Characters_Same('111'))
        self.assertTrue(all_Characters_Same(''))

    def test_edge_cases(self):
        self.assertTrue(all_Characters_Same('A'))
        self.assertTrue(all_Characters_Same(' '))

    def test_boundary_cases(self):
        self.assertFalse(all_Characters_Same('ab'))
        self.assertFalse(all_Characters_Same('aB'))
        self.assertFalse(all_Characters_Same('a '))

    def test_corner_cases(self):
        self.assertFalse(all_Characters_Same('abc'))
        self.assertFalse(all_Characters_Same('aBc'))
        self.assertFalse(all_Characters_Same('a b'))
