import unittest
from mbpp_235_code import even_bit_set_number

class TestEvenBitSetNumber(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(even_bit_set_number(0), 0)
        self.assertEqual(even_bit_set_number(1), 2)
        self.assertEqual(even_bit_set_number(2), 3)
        self.assertEqual(even_bit_set_number(3), 6)
        self.assertEqual(even_bit_set_number(4), 5)
        self.assertEqual(even_bit_set_number(5), 7)

    def test_edge_and_boundary_cases(self):
        self.assertEqual(even_bit_set_number(-1), 1)
        self.assertEqual(even_bit_set_number(0b1000_0000), 0b1000_0001)
        self.assertEqual(even_bit_set_number(0xFFFFFFFF), 0b1000_0000)
