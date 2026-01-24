import unittest
from mbpp_699_code import min_Swaps

class TestMinSwaps(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(min_Swaps('abc', 'abc'), 0)
        self.assertEqual(min_Swaps('abc', 'abcd'), 1)
        self.assertEqual(min_Swaps('abc', 'def'), 3)

    def test_empty(self):
        self.assertEqual(min_Swaps('', ''), 0)
        self.assertEqual(min_Swaps('abc', ''), 'Not Possible')
        self.assertEqual(min_Swaps('', 'abc'), 'Not Possible')

    def test_single_char(self):
        self.assertEqual(min_Swaps('a', 'a'), 0)
        self.assertEqual(min_Swaps('a', 'b'), 1)
        self.assertEqual(min_Swaps('a', 'c'), 1)

    def test_long_strings(self):
        self.assertEqual(min_Swaps('abcdefghijklmnopqrstuvwxyz', 'abcdefghijklmnopqrstuvwxyz'), 0)
        self.assertEqual(min_Swaps('abcdefghijklmnopqrstuvwxyz', 'abcdefghijklmnopqrstuvwxyz123'), 1)
        self.assertEqual(min_Swaps('abcdefghijklmnopqrstuvwxyz', 'defghijklmnopqrstuvwxyz'), 26)

    def test_non_integer(self):
        self.assertEqual(min_Swaps('abc', 'abc'), 0)
        self.assertEqual(min_Swaps('abc', 'abcd'), 1)
        self.assertEqual(min_Swaps('abc', 'def'), 3)
