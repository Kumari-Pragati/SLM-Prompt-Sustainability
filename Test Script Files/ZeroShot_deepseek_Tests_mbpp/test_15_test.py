import unittest
from mbpp_15_code import split_lowerstring

class TestSplitLowerString(unittest.TestCase):

    def test_split_lowerstring(self):
        self.assertEqual(split_lowerstring('abc'), ['abc'])
        self.assertEqual(split_lowerstring('aBc'), ['abc'])
        self.assertEqual(split_lowerstring('aBC'), ['aBC'])
        self.assertEqual(split_lowerstring('Abc'), ['Abc'])
        self.assertEqual(split_lowerstring('ABC'), ['ABC'])
        self.assertEqual(split_lowerstring('aBCd'), ['aBCd'])
        self.assertEqual(split_lowerstring('ABCd'), ['ABCd'])
        self.assertEqual(split_lowerstring('abc def'), ['abc', 'def'])
        self.assertEqual(split_lowerstring('aBC dEF'), ['aBC', 'dEF'])
        self.assertEqual(split_lowerstring('ABC DEF'), ['ABC', 'DEF'])
        self.assertEqual(split_lowerstring('aBCdef'), ['aBCdef'])
        self.assertEqual(split_lowerstring('ABCdef'), ['ABCdef'])
