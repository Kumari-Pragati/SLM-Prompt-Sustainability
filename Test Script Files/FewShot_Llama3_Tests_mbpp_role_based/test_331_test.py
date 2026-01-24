import unittest
from mbpp_331_code import count_unset_bits

class TestCountUnsetBits(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(count_unset_bits(0), 32)

    def test_power_of_two(self):
        self.assertEqual(count_unset_bits(2), 1)
        self.assertEqual(count_unset_bits(4), 2)
        self.assertEqual(count_unset_bits(8), 3)
        self.assertEqual(count_unset_bits(16), 4)

    def test_power_of_two_minus_one(self):
        self.assertEqual(count_unset_bits(1), 1)
        self.assertEqual(count_unset_bits(3), 2)
        self.assertEqual(count_unset_bits(7), 3)
        self.assertEqual(count_unset_bits(15), 4)

    def test_random_numbers(self):
        self.assertEqual(count_unset_bits(5), 2)
        self.assertEqual(count_unset_bits(10), 3)
        self.assertEqual(count_unset_bits(20), 5)
        self.assertEqual(count_unset_bits(30), 5)
