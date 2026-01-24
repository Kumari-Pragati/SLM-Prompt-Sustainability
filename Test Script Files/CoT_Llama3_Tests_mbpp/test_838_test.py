import unittest
from mbpp_838_code import min_Swaps

class TestMinSwaps(unittest.TestCase):
    def test_typical(self):
        self.assertEqual(min_Swaps('1010', '0101'), 2)
        self.assertEqual(min_Swaps('1111', '0000'), 2)
        self.assertEqual(min_Swaps('1010', '1010'), 0)
        self.assertEqual(min_Swaps('1111', '1111'), 0)

    def test_edge(self):
        self.assertEqual(min_Swaps('1000', '0100'), 1)
        self.assertEqual(min_Swaps('1110', '0001'), 1)
        self.assertEqual(min_Swaps('1010', '0110'), 1)
        self.assertEqual(min_Swaps('1100', '0011'), 1)

    def test_invalid(self):
        with self.assertRaises(TypeError):
            min_Swaps('1010', 'abc')
        with self.assertRaises(TypeError):
            min_Swaps('abc', '1010')
