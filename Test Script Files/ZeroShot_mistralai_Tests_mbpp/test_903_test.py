import unittest
from mbpp_903_code import count_Unset_Bits

class TestCountUnsetBits(unittest.TestCase):

    def test_zero(self):
        self.assertEqual(count_Unset_Bits(0), 1)

    def test_one(self):
        self.assertEqual(count_Unset_Bits(1), 1)

    def test_powers_of_two(self):
        for i in range(1, 11):
            self.assertEqual(count_Unset_Bits(2 ** i), i)

    def test_odd_numbers(self):
        for i in range(1, 11):
            self.assertEqual(count_Unset_Bits(2 * i + 1), i)

    def test_negative_numbers(self):
        for i in range(-10, 0):
            self.assertEqual(count_Unset_Bits(-i), count_Unset_Bits(i))

    def test_large_numbers(self):
        self.assertEqual(count_Unset_Bits(2 ** 31 - 1), 31)
        self.assertEqual(count_Unset_Bits(2 ** 64 - 1), 64)
