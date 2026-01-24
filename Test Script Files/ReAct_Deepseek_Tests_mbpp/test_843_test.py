import unittest
from mbpp_843_code import nth_super_ugly_number

class TestNthSuperUglyNumber(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(nth_super_ugly_number(10, [2, 7, 13, 19]), 238)

    def test_edge_case_n_equals_1(self):
        self.assertEqual(nth_super_ugly_number(1, [2, 3, 5]), 1)

    def test_edge_case_primes_empty(self):
        self.assertEqual(nth_super_ugly_number(5, []), 1)

    def test_edge_case_primes_single_prime(self):
        self.assertEqual(nth_super_ugly_number(5, [2]), 2)

    def test_edge_case_large_n(self):
        self.assertEqual(nth_super_ugly_number(1000, [2, 7, 13, 19]), 1000000000)

    def test_explicitly_handled_error_case_n_less_than_1(self):
        with self.assertRaises(ValueError):
            nth_super_ugly_number(0, [2, 3, 5])

    def test_explicitly_handled_error_case_negative_primes(self):
        with self.assertRaises(ValueError):
            nth_super_ugly_number(5, [-2, -3, -5])
