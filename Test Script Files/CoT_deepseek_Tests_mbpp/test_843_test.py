import unittest
from mbpp_843_code import nth_super_ugly_number

class TestNthSuperUglyNumber(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(nth_super_ugly_number(10, [2, 7, 13, 19]), 238)

    def test_single_prime(self):
        self.assertEqual(nth_super_ugly_number(5, [2]), 8)

    def test_same_prime(self):
        self.assertEqual(nth_super_ugly_number(6, [2, 2, 2]), 16)

    def test_large_n(self):
        self.assertEqual(nth_super_ugly_number(1000, [2, 3, 5]), 512000)

    def test_small_n(self):
        self.assertEqual(nth_super_ugly_number(1, [2, 3, 5]), 1)

    def test_empty_primes(self):
        with self.assertRaises(ValueError):
            nth_super_ugly_number(10, [])

    def test_negative_primes(self):
        with self.assertRaises(ValueError):
            nth_super_ugly_number(10, [-2, -3, -5])

    def test_zero_prime(self):
        with self.assertRaises(ValueError):
            nth_super_ugly_number(10, [0])

    def test_zero_n(self):
        self.assertEqual(nth_super_ugly_number(0, [2, 3, 5]), None)

    def test_negative_n(self):
        with self.assertRaises(ValueError):
            nth_super_ugly_number(-10, [2, 3, 5])
