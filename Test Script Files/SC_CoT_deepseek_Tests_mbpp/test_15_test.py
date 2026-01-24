import unittest
from mbpp_15_code import split_lowerstring

class TestSplitLowerString(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(split_lowerstring('abcDefGhi'), ['abc', 'Def', 'Ghi'])

    def test_single_letter(self):
        self.assertEqual(split_lowerstring('a'), ['a'])

    def test_empty_string(self):
        self.assertEqual(split_lowerstring(''), [])

    def test_all_lowercase(self):
        self.assertEqual(split_lowerstring('abcdefghi'), ['abcdefghi'])

    def test_all_uppercase(self):
        self.assertEqual(split_lowerstring('ABCDEFGHI'), ['ABCDEFGHI'])

    def test_numbers_and_symbols(self):
        self.assertEqual(split_lowerstring('a1b2c3d4'), ['a', '1b2', 'c3', 'd4'])

    def test_special_characters(self):
        self.assertEqual(split_lowerstring('a!b@c#d$e%f^g&h*i('), ['a', '!b@c#d$e%f^g&h*i('])

    def test_mixed_case(self):
        self.assertEqual(split_lowerstring('AbCDeFgHi'), ['AbCDeFgHi'])

    def test_boundary_case(self):
        self.assertEqual(split_lowerstring('a'*10000 + 'B'*10000), ['a'*10000])
