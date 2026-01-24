import unittest
from mbpp_843_code import nth_super_ugly_number

class TestNthSuperUglyNumber(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(nth_super_ugly_number(10, [2, 3, 5]), 32)
        self.assertEqual(nth_super_ugly_number(15, [2, 7, 13, 19]), 323)

    def test_single_prime(self):
        self.assertEqual(nth_super_ugly_number(10, [2]), 20)
        self.assertEqual(nth_super_ugly_number(10, [3]), 18)
        self.assertEqual(nth_super_ugly_number(10, [5]), 60)

    def test_empty_primes(self):
        with self.assertRaises(ValueError):
            nth_super_ugly_number(10, [])

    def test_single_number(self):
        with self.assertRaises(ValueError):
            nth_super_ugly_number(1, [2])

    def test_large_input(self):
        self.assertEqual(nth_super_ugly_number(100000, [2, 3, 5]), 12676506002)

    def test_small_input(self):
        self.assertEqual(nth_super_ugly_number(1, [2, 3, 5]), 1)
        self.assertEqual(nth_super_ugly_number(2, [2, 3, 5]), 7)
