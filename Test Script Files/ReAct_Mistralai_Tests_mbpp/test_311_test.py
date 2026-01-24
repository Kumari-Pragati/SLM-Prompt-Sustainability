import unittest
from mbpp_311_code import set_left_most_unset_bit

class TestSetLeftMostUnsetBit(unittest.TestCase):

    def test_empty(self):
        self.assertEqual(set_left_most_unset_bit(0), 1)

    def test_powers_of_two(self):
        for i in range(1, 32):
            self.assertEqual(set_left_most_unset_bit(1 << i), 1 << i)

    def test_negative_numbers(self):
        self.assertEqual(set_left_most_unset_bit(-1), -1)
        self.assertEqual(set_left_most_unset_bit(-2), -3)

    def test_all_bits_set(self):
        self.assertEqual(set_left_most_unset_bit(2**31 - 1), 2**31)

    def test_all_bits_unset(self):
        self.assertEqual(set_left_most_unset_bit(0), 1)

    def test_error_handling(self):
        with self.assertRaises(ValueError):
            set_left_most_unset_bit(-(2**32))
