import unittest
from mbpp_15_code import split_lowerstring

class TestSplitLowerstring(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(split_lowerstring('abc'), ['abc'])
        self.assertEqual(split_lowerstring('aBc'), ['a', 'Bc'])
        self.assertEqual(split_lowerstring('abc def'), ['abc', 'def'])
        self.assertEqual(split_lowerstring('aBc DeF'), ['a', 'Bc', 'DeF'])

    def test_edge_cases(self):
        self.assertEqual(split_lowerstring(''), [])
        self.assertEqual(split_lowerstring('ABC'), [])
        self.assertEqual(split_lowerstring('aBC'), ['a'])

    def test_corner_cases(self):
        self.assertEqual(split_lowerstring('a1b2c3'), ['a', '1b2c3'])
        self.assertEqual(split_lowerstring('a1B2c3'), ['a', '1', 'B2c3'])
