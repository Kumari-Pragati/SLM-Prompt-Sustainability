import unittest
from mbpp_671_code import set_Right_most_Unset_Bit

class TestSetRightmostUnsetBit(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(set_Right_most_Unset_Bit(0), 1)

    def test_single_bit(self):
        for i in range(1, 32):
            self.assertEqual(set_Right_most_Unset_Bit(i), i + 1)

    def test_multiple_bits(self):
        for i in range(32, 65):
            self.assertEqual(set_Right_most_Unset_Bit(i), i)

    def test_max_int(self):
        self.assertEqual(set_Right_most_Unset_Bit(2**31 - 1), 2**31)

    def test_min_int(self):
        self.assertEqual(set_Right_most_Unset_Bit(0), 1)

    def test_negative_numbers(self):
        for i in range(-32, 0):
            self.assertRaises(ValueError, set_Right_most_Unset_Bit, i)

    def test_non_integer_inputs(self):
        self.assertRaises(TypeError, set_Right_most_Unset_Bit, 3.14)
        self.assertRaises(TypeError, set_Right_most_Unset_Bit, "str")
