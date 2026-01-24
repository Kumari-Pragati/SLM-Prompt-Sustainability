import unittest
from mbpp_235_code import even_bit_set_number

class TestEvenBitSetNumber(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(even_bit_set_number(10), 14)

    def test_boundary_case(self):
        self.assertEqual(even_bit_set_number(0), 0)

    def test_edge_case(self):
        self.assertEqual(even_bit_set_number(2**31 - 1), 2**31 - 1)
        self.assertEqual(even_bit_set_number(2**31), 2**31)

    def test_special_case(self):
        self.assertEqual(even_bit_set_number(15), 15)
        self.assertEqual(even_bit_set_number(16), 32)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            even_bit_set_number("10")
