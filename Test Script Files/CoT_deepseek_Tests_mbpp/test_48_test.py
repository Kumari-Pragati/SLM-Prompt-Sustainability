import unittest
from mbpp_48_code import odd_bit_set_number

class TestOddBitSetNumber(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(odd_bit_set_number(0), 1)
        self.assertEqual(odd_bit_set_number(1), 3)
        self.assertEqual(odd_bit_set_number(2), 5)
        self.assertEqual(odd_bit_set_number(3), 7)
        self.assertEqual(odd_bit_set_number(4), 9)

    def test_edge_cases(self):
        self.assertEqual(odd_bit_set_number(1023), 1047)
        self.assertEqual(odd_bit_set_number(2047), 2111)
        self.assertEqual(odd_bit_set_number(4095), 4223)
        self.assertEqual(odd_bit_set_number(8191), 8455)
        self.assertEqual(odd_bit_set_number(16383), 16863)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            odd_bit_set_number("invalid")
        with self.assertRaises(TypeError):
            odd_bit_set_number(None)
        with self.assertRaises(TypeError):
            odd_bit_set_number([1, 2, 3])
