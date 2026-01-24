import unittest
from mbpp_741_code import all_Characters_Same

class TestAll_Characters_Same(unittest.TestCase):
    def test_typical_case(self):
        self.assertTrue(all_Characters_Same('aaaaaa'))
        self.assertTrue(all_Characters_Same('bbbbb'))
        self.assertTrue(all_Characters_Same('ccccc'))

    def test_edge_case(self):
        self.assertTrue(all_Characters_Same('a'))
        self.assertTrue(all_Characters_Same('b'))
        self.assertTrue(all_Characters_Same('c'))

    def test_corner_case(self):
        self.assertFalse(all_Characters_Same('abab'))
        self.assertFalse(all_Characters_Same('abcde'))
        self.assertFalse(all_Characters_Same('abcdef'))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            all_Characters_Same(123)
        with self.assertRaises(TypeError):
            all_Characters_Same([1, 2, 3])
