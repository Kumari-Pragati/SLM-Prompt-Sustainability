import unittest
from mbpp_45_code import get_gcd

class TestGetGCD(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(get_gcd([12, 16]), 4)
        self.assertEqual(get_gcd([36, 24]), 12)
        self.assertEqual(get_gcd([10, 2]), 2)

    def test_edge_case_zero(self):
        self.assertEqual(get_gcd([0, 10]), 10)
        self.assertEqual(get_gcd([10, 0]), 10)

    def test_edge_case_one(self):
        self.assertEqual(get_gcd([1, 10]), 1)

    def test_boundary_case_negative(self):
        self.assertEqual(get_gcd([-10, -2]), 2)
        self.assertEqual(get_gcd([-2, -10]), 2)

    def test_corner_case_single_number(self):
        self.assertEqual(get_gcd([10]), 10)
