import unittest
from mbpp_15_code import split_lowerstring

class TestSplitLowerstring(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(split_lowerstring('a'), ['a'])
        self.assertEqual(split_lowerstring('abc'), ['abc'])
        self.assertEqual(split_lowerstring('abcdef'), ['abcdef'])

    def test_edge_conditions(self):
        self.assertEqual(split_lowerstring(''), [])
        self.assertEqual(split_lowerstring('ABCDEF'), [])
        self.assertEqual(split_lowerstring('123456'), [])
        self.assertEqual(split_lowerstring('ABCDEFabcdef'), ['abcdef'])

    def test_complex_cases(self):
        self.assertEqual(split_lowerstring('aBcDeFgHiJkLmNoPqRsTuVwXyZ'), ['abcdefghijklmnopqrstuvwxyz'])
        self.assertEqual(split_lowerstring('aBcDeFgHiJkLmNoPqRsTuVwXyZ123456'), ['abcdefghijklmnopqrstuvwxyz'])
        self.assertEqual(split_lowerstring('ABCDEFabcdef'), ['abcdef'])
        self.assertEqual(split_lowerstring('aBCDeFgHiJkLmNoPqRsTuVwXyZ123456'), ['abcdef'])
