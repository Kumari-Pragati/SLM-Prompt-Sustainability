import unittest
from mbpp_48_code import odd_bit_set_number

class TestOddBitSetNumber(unittest.TestCase):
    def test_positive_number(self):
        self.assertEqual(odd_bit_set_number(5), 5)

    def test_negative_number(self):
        self.assertEqual(odd_bit_set_number(-5), -5)

    def test_zero(self):
        self.assertEqual(odd_bit_set_number(0), 0)

    def test_non_integer(self):
        with self.assertRaises(TypeError):
            odd_bit_set_number('a')

    def test_edge_case(self):
        self.assertEqual(odd_bit_set_number(2**31 - 1), 2**31 - 1)
