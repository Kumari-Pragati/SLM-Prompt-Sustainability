import unittest
from mbpp_311_code import set_left_most_unset_bit

class TestSetLeftMostUnsetBit(unittest.TestCase):
    def test_left_most_unset_bit(self):
        self.assertEqual(set_left_most_unset_bit(0), 1)
        self.assertEqual(set_left_most_unset_bit(5), 6)
        self.assertEqual(set_left_most_unset_bit(10), 11)
        self.assertEqual(set_left_most_unset_bit(2147483647), 2147483648)

    def test_right_most_set_bit(self):
        self.assertEqual(set_left_most_unset_bit(1), 2)
        self.assertEqual(set_left_most_unset_bit(255), 256)
        self.assertEqual(set_left_most_unset_bit(2147483648), 2147483649)

    def test_zero(self):
        self.assertEqual(set_left_most_unset_bit(0), 1)

    def test_negative_number(self):
        self.assertRaises(ValueError, set_left_most_unset_bit, -1)
