import unittest
from mbpp_671_code import set_Right_most_Unset_Bit

class TestSetRightmostUnsetBit(unittest.TestCase):
    def test_set_rightmost_unset_bit_positive_number(self):
        self.assertEqual(set_Right_most_Unset_Bit(10), 11)

    def test_set_rightmost_unset_bit_zero(self):
        self.assertEqual(set_Right_most_Unset_Bit(0), 1)

    def test_set_rightmost_unset_bit_power_of_two(self):
        self.assertEqual(set_Right_most_Unset_Bit(8), 8)

    def test_set_rightmost_unset_bit_power_of_two_minus_one(self):
        self.assertEqual(set_Right_most_Unset_Bit(7), 7)

    def test_set_rightmost_unset_bit_negative_number(self):
        self.assertEqual(set_Right_most_Unset_Bit(-10), -9)

    def test_set_rightmost_unset_bit_negative_power_of_two(self):
        self.assertEqual(set_Right_most_Unset_Bit(-8), -8)

    def test_set_rightmost_unset_bit_negative_power_of_two_minus_one(self):
        self.assertEqual(set_Right_most_Unset_Bit(-7), -7)
