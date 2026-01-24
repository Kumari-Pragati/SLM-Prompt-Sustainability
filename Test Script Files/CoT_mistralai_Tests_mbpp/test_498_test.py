import unittest
from498_code import gcd

class TestGCD(unittest.TestCase):
    def test_gcd_positive_numbers(self):
        self.assertEqual(gcd(36, 18), 6)
        self.assertEqual(gcd(25, 10), 5)
        self.assertEqual(gcd(498, 12), 12)
        self.assertEqual(gcd(1000, 500), 500)

    def test_gcd_negative_numbers(self):
        self.assertEqual(gcd(-36, -18), 6)
        self.assertEqual(gcd(-25, -10), 5)
        self.assertEqual(gcd(-498, -12), 12)
        self.assertEqual(gcd(-1000, -500), 500)

    def test_gcd_zero(self):
        self.assertEqual(gcd(0, 18), 0)
        self.assertEqual(gcd(36, 0), 0)
        self.assertEqual(gcd(-36, 0), 0)

    def test_gcd_one(self):
        self.assertEqual(gcd(1, 1), 1)
        self.assertEqual(gcd(-1, 1), 1)

    def test_gcd_prime_numbers(self):
        self.assertEqual(gcd(5, 7), 1)
        self.assertEqual(gcd(11, 13), 1)
        self.assertEqual(gcd(17, 19), 1)

    def test_gcd_large_numbers(self):
        self.assertEqual(gcd(987654321, 123456789), 7203)
        self.assertEqual(gcd(123456789, 987654321), 7203)
