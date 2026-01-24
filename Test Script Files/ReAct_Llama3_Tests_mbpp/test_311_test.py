import unittest
from mbpp_311_code import set_left_most_unset_bit

class TestSetLeftMostUnsetBit(unittest.TestCase):

    def test_set_left_most_unset_bit_positive(self):
        self.assertEqual(set_left_most_unset_bit(0), 0)
        self.assertEqual(set_left_most_unset_bit(1), 1)
        self.assertEqual(set_left_most_unset_bit(2), 2)
        self.assertEqual(set_left_most_unset_bit(3), 3)
        self.assertEqual(set_left_most_unset_bit(4), 4)
        self.assertEqual(set_left_most_unset_bit(5), 5)
        self.assertEqual(set_left_most_unset_bit(6), 6)
        self.assertEqual(set_left_most_unset_bit(7), 7)
        self.assertEqual(set_left_most_unset_bit(8), 8)
        self.assertEqual(set_left_most_unset_bit(9), 9)
        self.assertEqual(set_left_most_unset_bit(10), 10)

    def test_set_left_most_unset_bit_negative(self):
        self.assertEqual(set_left_most_unset_bit(-1), -1)
        self.assertEqual(set_left_most_unset_bit(-2), -2)
        self.assertEqual(set_left_most_unset_bit(-3), -3)
        self.assertEqual(set_left_most_unset_bit(-4), -4)
        self.assertEqual(set_left_most_unset_bit(-5), -5)
        self.assertEqual(set_left_most_unset_bit(-6), -6)
        self.assertEqual(set_left_most_unset_bit(-7), -7)
        self.assertEqual(set_left_most_unset_bit(-8), -8)
        self.assertEqual(set_left_most_unset_bit(-9), -9)
        self.assertEqual(set_left_most_unset_bit(-10), -10)

    def test_set_left_most_unset_bit_zero(self):
        self.assertEqual(set_left_most_unset_bit(0), 0)

    def test_set_left_most_unset_bit_edge_cases(self):
        self.assertEqual(set_left_most_unset_bit(0b11111111), 0b11111111)
        self.assertEqual(set_left_most_unset_bit(0b11111110), 0b11111111)
        self.assertEqual(set_left_most_unset_bit(0b11111100), 0b11111111)
        self.assertEqual(set_left_most_unset_bit(0b11111000), 0b11111111)
        self.assertEqual(set_left_most_unset_bit(0b11110000), 0b11111111)
        self.assertEqual(set_left_most_unset_bit(0b11100000), 0b11111111)
        self.assertEqual(set_left_most_unset_bit(0b11000000), 0b11111111)
        self.assertEqual(set_left_most_unset_bit(0b10000000), 0b11111111)
        self.assertEqual(set_left_most_unset_bit(0b00000000), 0b00000000)
