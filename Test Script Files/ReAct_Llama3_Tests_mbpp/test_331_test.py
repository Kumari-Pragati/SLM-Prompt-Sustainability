import unittest
from mbpp_331_code import count_unset_bits

class TestCountUnsetBits(unittest.TestCase):

    def test_zero(self):
        self.assertEqual(count_unset_bits(0), 0)

    def test_one(self):
        self.assertEqual(count_unset_bits(1), 0)

    def test_power_of_two(self):
        self.assertEqual(count_unset_bits(2), 1)
        self.assertEqual(count_unset_bits(4), 2)
        self.assertEqual(count_unset_bits(8), 3)
        self.assertEqual(count_unset_bits(16), 4)

    def test_power_of_two_minus_one(self):
        self.assertEqual(count_unset_bits(3), 2)
        self.assertEqual(count_unset_bits(7), 3)
        self.assertEqual(count_unset_bits(15), 4)
        self.assertEqual(count_unset_bits(31), 5)

    def test_random(self):
        self.assertEqual(count_unset_bits(5), 2)
        self.assertEqual(count_unset_bits(10), 2)
        self.assertEqual(count_unset_bits(20), 3)
        self.assertEqual(count_unset_bits(30), 4)

    def test_large(self):
        self.assertEqual(count_unset_bits(1000), 10)
        self.assertEqual(count_unset_bits(2000), 11)
        self.assertEqual(count_unset_bits(3000), 12)
