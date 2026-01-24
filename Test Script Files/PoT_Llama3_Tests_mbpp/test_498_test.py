import unittest
from mbpp_498_code import gcd

class TestGCD(unittest.TestCase):
    def test_typical_cases(self):
        self.assertEqual(gcd(12, 15), 3)
        self.assertEqual(gcd(24, 30), 6)
        self.assertEqual(gcd(48, 18), 6)
        self.assertEqual(gcd(36, 12), 12)
        self.assertEqual(gcd(9, 15), 3)

    def test_edge_cases(self):
        self.assertEqual(gcd(0, 0), 0)
        self.assertEqual(gcd(0, 1), 1)
        self.assertEqual(gcd(1, 0), 1)
        self.assertEqual(gcd(1, 1), 1)
        self.assertEqual(gcd(2, 3), 1)

    def test_corner_cases(self):
        self.assertEqual(gcd(4, 4), 4)
        self.assertEqual(gcd(8, 8), 8)
        self.assertEqual(gcd(12, 12), 12)
