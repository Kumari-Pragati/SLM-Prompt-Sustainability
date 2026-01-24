import unittest
from mbpp_235_code import even_bit_set_number

class TestEvenBitSetNumber(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(even_bit_set_number(0), 0)
        self.assertEqual(even_bit_set_number(1), 3)
        self.assertEqual(even_bit_set_number(2), 2)
        self.assertEqual(even_bit_set_number(3), 3)
        self.assertEqual(even_bit_set_number(4), 4)
        self.assertEqual(even_bit_set_number(5), 7)
        self.assertEqual(even_bit_set_number(6), 6)
        self.assertEqual(even_bit_set_number(7), 7)

    def test_edge_cases(self):
        self.assertEqual(even_bit_set_number(8), 8)
        self.assertEqual(even_bit_set_number(9), 15)
        self.assertEqual(even_bit_set_number(10), 10)
        self.assertEqual(even_bit_set_number(11), 11)
        self.assertEqual(even_bit_set_number(12), 12)
        self.assertEqual(even_bit_set_number(13), 15)
        self.assertEqual(even_bit_set_number(14), 14)
        self.assertEqual(even_bit_set_number(15), 15)

    def test_boundary_cases(self):
        self.assertEqual(even_bit_set_number(16), 16)
        self.assertEqual(even_bit_set_number(17), 31)
        self.assertEqual(even_bit_set_number(18), 18)
        self.assertEqual(even_bit_set_number(19), 19)
        self.assertEqual(even_bit_set_number(20), 20)
        self.assertEqual(even_bit_set_number(21), 31)
        self.assertEqual(even_bit_set_number(22), 22)
        self.assertEqual(even_bit_set_number(23), 23)
