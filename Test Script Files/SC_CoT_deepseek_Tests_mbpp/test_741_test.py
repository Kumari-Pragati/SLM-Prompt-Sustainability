import unittest

from mbpp_741_code import all_Characters_Same

class TestAllCharactersSame(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(all_Characters_Same('aaa'))
        self.assertTrue(all_Characters_Same('111'))
        self.assertTrue(all_Characters_Same('True'))

    def test_edge_cases(self):
        self.assertTrue(all_Characters_Same(''))
        self.assertTrue(all_Characters_Same(' '))

    def test_corner_cases(self):
        self.assertTrue(all_Characters_Same('A'))
        self.assertTrue(all_Characters_Same('a'))
        self.assertTrue(all_Characters_Same('0'))

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            all_Characters_Same(123)
        with self.assertRaises(TypeError):
            all_Characters_Same(None)
        with self.assertRaises(TypeError):
            all_Characters_Same(['a', 'b', 'c'])
