import unittest
from mbpp_498_code import gcd

class TestGCD(unittest.TestCase):

    def test_gcd_positive_numbers(self):
        self.assertEqual(gcd(12, 15), 3)
        self.assertEqual(gcd(24, 30), 6)
        self.assertEqual(gcd(48, 18), 6)
        self.assertEqual(gcd(36, 42), 6)
        self.assertEqual(gcd(18, 24), 6)
        self.assertEqual(gcd(15, 12), 3)
        self.assertEqual(gcd(30, 24), 6)
        self.assertEqual(gcd(18, 36), 6)
        self.assertEqual(gcd(24, 48), 12)
        self.assertEqual(gcd(42, 36), 6)
        self.assertEqual(gcd(12, 12), 12)

    def test_gcd_negative_numbers(self):
        self.assertEqual(gcd(-12, 15), 3)
        self.assertEqual(gcd(-24, 30), 6)
        self.assertEqual(gcd(-48, 18), 6)
        self.assertEqual(gcd(-36, 42), 6)
        self.assertEqual(gcd(-18, 24), 6)
        self.assertEqual(gcd(-15, 12), 3)
        self.assertEqual(gcd(-30, 24), 6)
        self.assertEqual(gcd(-18, 36), 6)
        self.assertEqual(gcd(-24, 48), 12)
        self.assertEqual(gcd(-42, 36), 6)
        self.assertEqual(gcd(-12, -12), 12)

    def test_gcd_zero(self):
        self.assertEqual(gcd(0, 15), 15)
        self.assertEqual(gcd(0, 0), 0)
        self.assertEqual(gcd(12, 0), 12)
        self.assertEqual(gcd(15, 0), 15)
        self.assertEqual(gcd(0, 12), 12)
        self.assertEqual(gcd(12, 12), 12)

    def test_gcd_non_integer(self):
        self.assertEqual(gcd(12.0, 15), 3)
        self.assertEqual(gcd(24.0, 30), 6)
        self.assertEqual(gcd(48.0, 18), 6)
        self.assertEqual(gcd(36.0, 42), 6)
        self.assertEqual(gcd(18.0, 24), 6)
        self.assertEqual(gcd(15.0, 12), 3)
        self.assertEqual(gcd(30.0, 24), 6)
        self.assertEqual(gcd(18.0, 36), 6)
        self.assertEqual(gcd(24.0, 48), 12)
        self.assertEqual(gcd(42.0, 36), 6)
        self.assertEqual(gcd(12.0, 12.0), 12)
