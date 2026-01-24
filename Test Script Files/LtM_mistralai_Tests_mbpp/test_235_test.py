import unittest
from mbpp_235_code import even_bit_set_number

class TestEvenBitSetNumber(unittest.TestCase):

    def test_simple_even(self):
        self.assertEqual(even_bit_set_number(4), 6)

    def test_simple_odd(self):
        self.assertEqual(even_bit_set_number(5), 7)

    def test_edge_min(self):
        self.assertEqual(even_bit_set_number(0), 0)

    def test_edge_max(self.test_edge_max_positive):
        self.assertEqual(even_bit_set_number(2**31 - 1), 2**31 - 1)

    def test_edge_max_negative(self):
        self.assertEqual(even_bit_set_number(-(2**31)), -(2**31))

    def test_combined_even(self):
        self.assertEqual(even_bit_set_number(10), 14)

    def test_combined_odd(self):
        self.assertEqual(even_bit_set_number(11), 13)

    def test_invalid_input_zero(self):
        with self.assertRaises(ValueError):
            even_bit_set_number(0)
