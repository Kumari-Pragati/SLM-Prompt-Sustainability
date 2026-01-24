import unittest
from mbpp_595_code import min_Swaps

class TestMinSwaps(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(min_Swaps('abc', 'abc'), 0)
        self.assertEqual(min_Swaps('abc', 'abcd'), 1)
        self.assertEqual(min_Swaps('abc', 'def'), 3)

    def test_edge(self):
        self.assertEqual(min_Swaps('', ''), 0)
        self.assertEqual(min_Swaps('a', ''), 'Not Possible')
        self.assertEqual(min_Swaps('', 'a'), 'Not Possible')

    def test_complex(self):
        self.assertEqual(min_Swaps('abc', 'def'), 3)
        self.assertEqual(min_Swaps('abc', 'defgh'), 4)
        self.assertEqual(min_Swaps('abc', 'defghij'), 5)

    def test_invalid(self):
        with self.assertRaises(TypeError):
            min_Swaps(123, 'abc')
        with self.assertRaises(TypeError):
            min_Swaps('abc', 123)
