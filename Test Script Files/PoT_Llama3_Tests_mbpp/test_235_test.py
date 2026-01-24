import unittest
from mbpp_235_code import even_bit_set_number

class TestEvenBitSetNumber(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(even_bit_set_number(5), 7)

    def test_edge_case_zero(self):
        self.assertEqual(even_bit_set_number(0), 0)

    def test_edge_case_one(self):
        self.assertEqual(even_bit_set_number(1), 1)

    def test_edge_case_power_of_two(self):
        self.assertEqual(even_bit_set_number(8), 8)

    def test_edge_case_power_of_two_plus_one(self):
        self.assertEqual(even_bit_set_number(9), 9)

    def test_edge_case_negative_number(self):
        with self.assertRaises(TypeError):
            even_bit_set_number(-1)

    def test_edge_case_non_integer(self):
        with self.assertRaises(TypeError):
            even_bit_set_number(3.14)
