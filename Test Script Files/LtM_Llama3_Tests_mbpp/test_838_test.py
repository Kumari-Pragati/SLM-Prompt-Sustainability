import unittest
from mbpp_838_code import min_Swaps

class TestMinSwaps(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(min_Swaps('0000', '1111'), 2)
        self.assertEqual(min_Swaps('1111', '0000'), 2)
        self.assertEqual(min_Swaps('1010', '0101'), 2)
        self.assertEqual(min_Swaps('1110', '0001'), 2)

    def test_edge(self):
        self.assertEqual(min_Swaps('', ''), 0)
        self.assertEqual(min_Swaps('0', '1'), 1)
        self.assertEqual(min_Swaps('1', '0'), 1)
        self.assertEqual(min_Swaps('1111', '0000'), 2)

    def test_invalid(self):
        with self.assertRaises(TypeError):
            min_Swaps('a', 'b')
        with self.assertRaises(TypeError):
            min_Swaps('0', 'abc')

    def test_complex(self):
        self.assertEqual(min_Swaps('101010', '010101'), 2)
        self.assertEqual(min_Swaps('111111', '000000'), 2)
        self.assertEqual(min_Swaps('10101010', '01010101'), 2)
