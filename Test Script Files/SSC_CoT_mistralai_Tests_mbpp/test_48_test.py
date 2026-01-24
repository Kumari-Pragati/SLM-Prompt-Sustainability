import unittest
from mbpp_48_code import odd_bit_set_number

class TestOddBitSetNumber(unittest.TestCase):

    def test_typical_input(self):
        self.assertEqual(odd_bit_set_number(5), 7)
        self.assertEqual(odd_bit_set_number(21), 29)
        self.assertEqual(odd_bit_set_number(1023), 1027)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(odd_bit_set_number(0), 1)
        self.assertEqual(odd_bit_set_number(1), 3)
        self.assertEqual(odd_bit_set_number(2**31 - 1), 2**31)
        self.assertEqual(odd_bit_set_number(2**31), 2**32 - 1)

    def test_special_cases(self):
        self.assertEqual(odd_bit_set_number(2), 3)
        self.assertEqual(odd_bit_set_number(4), 5)
        self.assertEqual(odd_bit_set_number(6), 7)
