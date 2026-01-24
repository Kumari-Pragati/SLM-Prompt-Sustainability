import unittest
from mbpp_331_code import count_unset_bits

class TestCountUnsetBits(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(count_unset_bits(0), 1)

    def test_one(self):
        self.assertEqual(count_unset_bits(1), 1)

    def test_power_of_two(self):
        self.assertEqual(count_unset_bits(2), 1)
        self.assertEqual(count_unset_bits(4), 2)
        self.assertEqual(count_unset_bits(8), 3)
        self.assertEqual(count_unset_bits(16), 4)

    def test_odd_numbers(self):
        self.assertEqual(count_unset_bits(3), 2)
        self.assertEqual(count_unset_bits(5), 2)
        self.assertEqual(count_unset_bits(7), 3)

    def test_negative_numbers(self):
        self.assertEqual(count_unset_bits(-1), 0)
        self.assertEqual(count_unset_bits(-2), 1)
        self.assertEqual(count_unset_bits(-3), 1)

    def test_large_numbers(self):
        self.assertEqual(count_unset_bits(2147483647), 31)
        self.assertEqual(count_unset_bits(2147483648), 1)
