import unittest
from mbpp_48_code import odd_bit_set_number

class TestOddBitSetNumber(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(odd_bit_set_number(1), 3)
        self.assertEqual(odd_bit_set_number(2), 3)
        self.assertEqual(odd_bit_set_number(4), 5)
        self.assertEqual(odd_bit_set_number(7), 7)
        self.assertEqual(odd_bit_set_number(8), 9)
        self.assertEqual(odd_bit_set_number(15), 15)

    def test_edge_and_boundary_cases(self):
        self.assertEqual(odd_bit_set_number(0), 1)
        self.assertEqual(odd_bit_set_number(16), 17)
        self.assertEqual(odd_bit_set_number(32), 33)
        self.assertEqual(odd_bit_set_number(63), 63)
        self.assertEqual(odd_bit_set_number(127), 129)
        self.assertEqual(odd_bit_set_number(255), 255)
