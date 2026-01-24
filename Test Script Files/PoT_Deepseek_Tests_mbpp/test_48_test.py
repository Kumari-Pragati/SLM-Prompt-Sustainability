import unittest
from mbpp_48_code import odd_bit_set_number

class TestOddBitSetNumber(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(odd_bit_set_number(0), 1)
        self.assertEqual(odd_bit_set_number(1), 3)
        self.assertEqual(odd_bit_set_number(2), 5)
        self.assertEqual(odd_bit_set_number(3), 7)
        self.assertEqual(odd_bit_set_number(4), 9)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(odd_bit_set_number(255), 511)
        self.assertEqual(odd_bit_set_number(1023), 2047)
        self.assertEqual(odd_bit_set_number(4095), 8191)

    def test_corner_cases(self):
        self.assertEqual(odd_bit_set_number(8191), 16383)
        self.assertEqual(odd_bit_set_number(16383), 32767)
        self.assertEqual(odd_bit_set_number(32767), 65535)
        self.assertEqual(odd_bit_set_number(65535), 131071)
