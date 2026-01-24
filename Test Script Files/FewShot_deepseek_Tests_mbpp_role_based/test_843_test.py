import unittest
from mbpp_843_code import nth_super_ugly_number

class TestNthSuperUglyNumber(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(nth_super_ugly_number(10, [2, 7, 13, 19]), 12)

    def test_edge_case_with_single_prime(self):
        self.assertEqual(nth_super_ugly_number(5, [2]), 4)

    def test_boundary_condition_with_large_input(self):
        self.assertEqual(nth_super_ugly_number(1000, [2, 7, 13, 19]), 1000)

    def test_boundary_condition_with_small_input(self):
        self.assertEqual(nth_super_ugly_number(1, [2, 7, 13, 19]), 1)

    def test_error_handling_with_invalid_n(self):
        with self.assertRaises(ValueError):
            nth_super_ugly_number(-10, [2, 7, 13, 19])

    def test_error_handling_with_invalid_primes(self):
        with self.assertRaises(ValueError):
            nth_super_ugly_number(10, [])
