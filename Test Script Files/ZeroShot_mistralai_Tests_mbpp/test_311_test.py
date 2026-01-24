import unittest
from mbpp_311_code import set_left_most_unset_bit

class TestSetLeftMostUnsetBit(unittest.TestCase):

    def test_zero(self):
        self.assertEqual(set_left_most_unset_bit(0), 1)

    def test_one(self):
        self.assertEqual(set_left_most_unset_bit(1), 2)

    def test_powers_of_two(self):
        for i in range(1, 32):
            self.assertEqual(set_left_most_unset_bit(1 << i), 1 << (i - 1))

    def test_negative_numbers(self):
        self.assertEqual(set_left_most_unset_bit(-1), -2)

    def test_large_numbers(self):
        self.assertEqual(set_left_most_unset_bit(2147483647), 2147483646)

    def test_edge_cases(self):
        self.assertEqual(set_left_most_unset_bit(2147483648), 2147483648)
        self.assertEqual(set_left_most_unset_bit(0xFFFFFFFF), 0)
