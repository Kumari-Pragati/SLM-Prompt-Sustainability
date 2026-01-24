import unittest
from mbpp_311_code import set_left_most_unset_bit

class TestSetLeftMostUnsetBit(unittest.TestCase):
    def test_set_left_most_unset_bit_positive(self):
        self.assertEqual(set_left_most_unset_bit(5), 7)

    def test_set_left_most_unset_bit_negative(self):
        self.assertEqual(set_left_most_unset_bit(-5), -5)

    def test_set_left_most_unset_bit_zero(self):
        self.assertEqual(set_left_most_unset_bit(0), 0)

    def test_set_left_most_unset_bit_all_unset(self):
        self.assertEqual(set_left_most_unset_bit(0b1111), 0b1111)

    def test_set_left_most_unset_bit_all_set(self):
        self.assertEqual(set_left_most_unset_bit(0b1111), 0b1111)

    def test_set_left_most_unset_bit_no_unset_bit(self):
        self.assertEqual(set_left_most_unset_bit(0b1110), 0b1111)
