import unittest
from mbpp_45_code import get_gcd

class TestGetGcd(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(get_gcd([48, 18]), 6)

    def test_edge_case_single_number(self):
        self.assertEqual(get_gcd([48]), 48)

    def test_boundary_case_zero(self):
        self.assertEqual(get_gcd([0, 18]), 18)
        self.assertEqual(get_gcd([48, 0]), 48)

    def test_boundary_case_negative_numbers(self):
        self.assertEqual(get_gcd([-48, -18]), 6)
        self.assertEqual(get_gcd([48, -18]), 6)
        self.assertEqual(get_gcd([-48, 18]), 6)

    def test_corner_case_same_numbers(self):
        self.assertEqual(get_gcd([48, 48]), 48)

    def test_corner_case_zero_and_same_number(self):
        self.assertEqual(get_gcd([0, 48]), 48)
        self.assertEqual(get_gcd([48, 0]), 48)

    def test_corner_case_multiple_zeros(self):
        self.assertEqual(get_gcd([0, 0, 0]), 0)

    def test_corner_case_large_numbers(self):
        self.assertEqual(get_gcd([1000000000, 2000000000]), 1000000000)
