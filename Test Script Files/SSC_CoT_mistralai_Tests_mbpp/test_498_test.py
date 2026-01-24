import unittest
from mbpp_498_code import gcd

class TestGCD(unittest.TestCase):

    def test_gcd_normal(self):
        self.assertEqual(gcd(36, 21), 3)
        self.assertEqual(gcd(12, 18), 6)
        self.assertEqual(gcd(25, 10), 5)

    def test_gcd_edge_cases(self):
        self.assertEqual(gcd(0, 4), 4)
        self.assertEqual(gcd(4, 0), 4)
        self.assertEqual(gcd(1, 1), 1)
        self.assertEqual(gcd(-1, 1), 1)
        self.assertEqual(gcd(1, -1), 1)

    def test_gcd_boundary_cases(self):
        self.assertEqual(gcd(1, 0), 1)
        self.assertEqual(gcd(0, 1), 1)
        self.assertEqual(gcd(1, 1000000), 1)
        self.assertEqual(gcd(1000000, 1), 1)

    def test_gcd_negative(self):
        self.assertEqual(gcd(-3, 4), 1)
        self.assertEqual(gcd(-4, 3), 1)
        self.assertEqual(gcd(-3, -4), 3)
