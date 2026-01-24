import unittest
from mbpp_45_code import get_gcd

class TestGetGCD(unittest.TestCase):
    def test_normal_inputs(self):
        self.assertEqual(get_gcd([36, 216]), 36)
        self.assertEqual(get_gcd([12, 18]), 6)
        self.assertEqual(get_gcd([8, 24]), 8)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(get_gcd([0, 12]), 12)
        self.assertEqual(get_gcd([12, 0]), 12)
        self.assertEqual(get_gcd([-12, 12]), 12)
        self.assertEqual(get_gcd([12, -12]), 12)
        self.assertEqual(get_gcd([1, 1]), 1)
        self.assertEqual(get_gcd([1, 0]), 1)
        self.assertEqual(get_gcd([0, 1]), 1)

    def test_special_cases(self):
        self.assertEqual(get_gcd([1, 2]), 1)
        self.assertEqual(get_gcd([2, 1]), 1)
        self.assertEqual(get_gcd([1, 3]), 1)
        self.assertEqual(get_gcd([3, 1]), 1)
        self.assertEqual(get_gcd([1, 4]), 1)
        self.assertEqual(get_gcd([4, 1]), 1)
        self.assertEqual(get_gcd([1, 5]), 1)
        self.assertEqual(get_gcd([5, 1]), 1)
