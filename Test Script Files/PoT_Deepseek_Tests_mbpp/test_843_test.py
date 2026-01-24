import unittest
from mbpp_843_code import nth_super_ugly_number

class TestNthSuperUglyNumber(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(nth_super_ugly_number(10, [2, 7, 13, 19]), 238)

    def test_edge_case_n_equals_1(self):
        self.assertEqual(nth_super_ugly_number(1, [2, 3, 5]), 1)

    def test_edge_case_primes_empty(self):
        self.assertEqual(nth_super_ugly_number(5, []), 1)

    def test_boundary_case_large_n(self):
        self.assertEqual(nth_super_ugly_number(1000, [2, 7, 13, 19]), 10000000)

    def test_corner_case_large_primes(self):
        self.assertEqual(nth_super_ugly_number(10, [1000000000, 1000000000, 1000000000]), 10000000000000000)

    def test_corner_case_small_primes(self):
        self.assertEqual(nth_super_ugly_number(10, [2, 3, 5]), 238)

    def test_invalid_input_n_less_than_1(self):
        with self.assertRaises(AssertionError):
            nth_super_ugly_number(0, [2, 3, 5])

    def test_invalid_input_negative_primes(self):
        with self.assertRaises(AssertionError):
            nth_super_ugly_number(10, [-2, -3, -5])
