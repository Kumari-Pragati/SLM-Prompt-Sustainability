import unittest
from mbpp_48_code import odd_bit_set_number

class TestOddBitSetNumber(unittest.TestCase):
    def test_typical_inputs(self):
        self.assertEqual(odd_bit_set_number(1), 3)
        self.assertEqual(odd_bit_set_number(5), 7)
        self.assertEqual(odd_bit_set_number(21), 29)

    def test_edge_cases(self):
        self.assertEqual(odd_bit_set_number(0), 1)
        self.assertEqual(odd_bit_set_number(1023), 1025)
        self.assertEqual(odd_bit_set_number(2**31 - 1), 2**31 - 1)

    def test_boundary_conditions(self):
        self.assertEqual(odd_bit_set_number(2**31), 2**31)
        self.assertEqual(odd_bit_set_number(-1), -1)
        self.assertEqual(odd_bit_set_number(-2**31), -2**31)

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, odd_bit_set_number, "string")
        self.assertRaises(TypeError, odd_bit_set_number, 2.5)
        self.assertRaises(TypeError, odd_bit_set_number, [1, 2, 3])
