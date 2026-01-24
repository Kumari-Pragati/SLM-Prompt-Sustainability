import unittest
from mbpp_843_code import nth_super_ugly_number

class TestNthSuperUglyNumber(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(nth_super_ugly_number(10, [2, 3, 5]), 32)
        self.assertEqual(nth_super_ugly_number(15, [2, 7, 13, 19]), 323)

    def test_edge_case_single_prime(self):
        self.assertEqual(nth_super_ugly_number(10, [2]), 20)
        self.assertEqual(nth_super_ugly_number(10, [3]), 18)
        self.assertEqual(nth_super_ugly_number(10, [5]), 25)

    def test_edge_case_two_primes(self):
        self.assertEqual(nth_super_ugly_number(10, [2, 3]), 24)
        self.assertEqual(nth_super_ugly_number(10, [3, 2]), 24)
        self.assertEqual(nth_super_ugly_number(10, [5, 2]), 30)
        self.assertEqual(nth_super_ugly_number(10, [2, 5]), 30)

    def test_edge_case_three_primes(self):
        self.assertEqual(nth_super_ugly_number(10, [2, 3, 5]), 32)
        self.assertEqual(nth_super_ugly_number(10, [3, 2, 5]), 32)
        self.assertEqual(nth_super_ugly_number(10, [5, 2, 3]), 32)
        self.assertEqual(nth_super_ugly_number(10, [5, 3, 2]), 32)

    def test_boundary_case_small_n(self):
        self.assertEqual(nth_super_ugly_number(1, [2, 3, 5]), 1)
        self.assertEqual(nth_super_ugly_number(2, [2, 3, 5]), 2)
        self.assertEqual(nth_super_ugly_number(3, [2, 3, 5]), 6)

    def test_boundary_case_large_n(self):
        self.assertEqual(nth_super_ugly_number(1000, [2, 3, 5]), 665857)
        self.assertEqual(nth_super_ugly_number(1000, [2, 7, 13, 19]), 1316455980)
