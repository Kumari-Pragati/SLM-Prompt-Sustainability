import unittest
from mbpp_311_code import set_left_most_unset_bit

class TestSetLeftMostUnsetBit(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(set_left_most_unset_bit(0), 1)
        self.assertEqual(set_left_most_unset_bit(1), 3)
        self.assertEqual(set_left_most_unset_bit(15), 16)
        self.assertEqual(set_left_most_unset_bit(255), 256)
        self.assertEqual(set_left_most_unset_bit(2147483647), 2147483648)

    def test_edge_cases(self):
        self.assertEqual(set_left_most_unset_bit(1), 3)
        self.assertEqual(set_left_most_unset_bit(2), 3)
        self.assertEqual(set_left_most_unset_bit(4), 5)
        self.assertEqual(set_left_most_unset_bit(5), 6)
        self.assertEqual(set_left_most_unset_bit(6), 6)
        self.assertEqual(set_left_most_unset_bit(7), 8)

    def test_corner_cases(self):
        self.assertEqual(set_left_most_unset_bit(0), 1)
        self.assertEqual(set_left_most_unset_bit(1), 3)
        self.assertEqual(set_left_most_unset_bit(2**31 - 1), 2**31)
        self.assertEqual(set_left_most_unset_bit(2**31), 2**32)
        self.assertEqual(set_left_most_unset_bit(2**64 - 1), 2**64)
        self.assertEqual(set_left_most_unset_bit(2**64), 2**65)
