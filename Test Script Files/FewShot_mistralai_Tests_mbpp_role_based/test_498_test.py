import unittest
from mbpp_498_code import gcd

class TestGCD(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(gcd(25, 10), 5)
        self.assertEqual(gcd(36, 18), 6)
        self.assertEqual(gcd(12, 18), 6)

    def test_zero(self):
        self.assertEqual(gcd(0, 0), 0)
        self.assertEqual(gcd(0, 1), 1)
        self.assertEqual(gcd(1, 0), 1)

    def test_negative_numbers(self):
        self.assertEqual(gcd(-25, 10), 5)
        self.assertEqual(gcd(-36, 18), 6)
        self.assertEqual(gcd(-12, 18), 6)

    def test_one(self):
        self.assertEqual(gcd(1, 1), 1)

    def test_large_numbers(self):
        self.assertEqual(gcd(987654321, 123456789), 7)

    def test_small_numbers(self):
        self.assertEqual(gcd(2, 3), 1)

    def test_divisibility_by_zero(self):
        with self.assertRaises(ValueError):
            gcd(0, 0)
