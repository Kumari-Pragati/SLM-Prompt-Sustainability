import unittest
from mbpp_903_code import count_Unset_Bits

class TestCountUnsetBits(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(count_Unset_Bits(0), 0)

    def test_one(self):
        self.assertEqual(count_Unset_Bits(1), 0)

    def test_power_of_two(self):
        self.assertEqual(count_Unset_Bits(2), 1)
        self.assertEqual(count_Unset_Bits(4), 2)
        self.assertEqual(count_Unset_Bits(8), 3)

    def test_power_of_two_offset(self):
        self.assertEqual(count_Unset_Bits(3), 1)
        self.assertEqual(count_Unset_Bits(5), 2)
        self.assertEqual(count_Unset_Bits(7), 3)

    def test_random_numbers(self):
        self.assertEqual(count_Unset_Bits(10), 1)
        self.assertEqual(count_Unset_Bits(15), 3)
        self.assertEqual(count_Unset_Bits(20), 4)

    def test_large_number(self):
        self.assertEqual(count_Unset_Bits(1024), 10)
