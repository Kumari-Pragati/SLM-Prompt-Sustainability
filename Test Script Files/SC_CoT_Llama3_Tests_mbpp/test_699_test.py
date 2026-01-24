import unittest
from mbpp_699_code import min_Swaps

class TestMinSwaps(unittest.TestCase):

    def test_typical_inputs(self):
        self.assertEqual(min_Swaps('abc', 'def'), 2)
        self.assertEqual(min_Swaps('hello', 'world'), 4)
        self.assertEqual(min_Swaps('abc', 'abc'), 0)

    def test_edge_cases(self):
        self.assertEqual(min_Swaps('a', 'a'), 0)
        self.assertEqual(min_Swaps('a', 'b'), 1)
        self.assertEqual(min_Swaps('ab', 'ba'), 1)

    def test_special_cases(self):
        self.assertEqual(min_Swaps('abc', 'def'), 2)
        self.assertEqual(min_Swaps('abc', 'defgh'), 3)
        self.assertEqual(min_Swaps('abcdef', 'defghij'), 4)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            min_Swaps(123, 'abc')
        with self.assertRaises(TypeError):
            min_Swaps('abc', 123)
