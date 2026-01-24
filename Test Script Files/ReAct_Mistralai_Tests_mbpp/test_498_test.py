import unittest
from mbpp_498_code import gcd

class TestGCD(unittest.TestCase):

    def test_gcd_positive_numbers(self):
        self.assertEqual(gcd(36, 18), 6)
        self.assertEqual(gcd(25, 10), 5)
        self.assertEqual(gcd(498, 12), 12)
        self.assertEqual(gcd(1000, 500), 1)

    def test_gcd_negative_numbers(self):
        self.assertEqual(gcd(-36, -18), 6)
        self.assertEqual(gcd(-25, -10), 5)
        self.assertEqual(gcd(-498, -12), 12)
        self.assertEqual(gcd(-1000, -500), 1)

    def test_gcd_zero(self):
        self.assertEqual(gcd(0, 10), 0)
        self.assertEqual(gcd(10, 0), 0)
        self.assertEqual(gcd(0, 0), 0)

    def test_gcd_one(self):
        self.assertEqual(gcd(1, 1), 1)
        self.assertEqual(gcd(1, 2), 1)
        self.assertEqual(gcd(2, 1), 1)

    def test_gcd_large_numbers(self):
        self.assertEqual(gcd(2**64, 2**64 - 1), 1)
        self.assertEqual(gcd(2**64 - 1, 2**64), 1)

    def test_gcd_small_numbers(self):
        self.assertEqual(gcd(1, 2), 1)
        self.assertEqual(gcd(2, 1), 1)
        self.assertEqual(gcd(1, 3), 1)
        self.assertEqual(gcd(3, 1), 1)

    def test_gcd_floats(self):
        self.assertEqual(gcd(10.5, 3.5), 1)
        self.assertEqual(gcd(10.5, 7), 1)
        self.assertEqual(gcd(7, 10.5), 1)
