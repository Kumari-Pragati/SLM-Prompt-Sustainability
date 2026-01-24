import unittest
from mbpp_498_code import gcd

class TestGCD(unittest.TestCase):

    def test_gcd_simple(self):
        self.assertEqual(gcd(3, 1), 1)
        self.assertEqual(gcd(3, 2), 1)
        self.assertEqual(gcd(3, 3), 3)
        self.assertEqual(gcd(4, 2), 2)
        self.assertEqual(gcd(8, 16), 8)

    def test_gcd_negative(self):
        self.assertEqual(gcd(-3, 1), 1)
        self.assertEqual(gcd(-3, -2), 1)
        self.assertEqual(gcd(-3, -3), 3)
        self.assertEqual(gcd(-4, -2), 2)
        self.assertEqual(gcd(-8, -16), 8)

    def test_gcd_zero(self):
        self.assertEqual(gcd(0, 1), 1)
        self.assertEqual(gcd(0, 0), 0)
        self.assertEqual(gcd(0, -1), 1)
        self.assertEqual(gcd(-0, 1), 1)
        self.assertEqual(gcd(-0, -1), 1)

    def test_gcd_large(self):
        self.assertEqual(gcd(123456789, 987654321), 72576051)
        self.assertEqual(gcd(1234567890, 9876543210), 1000000009)
