import unittest
from mbpp_687_code import recur_gcd

class TestRecurGCD(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(recur_gcd(48, 18), 6)
        self.assertEqual(recur_gcd(81, 27), 9)
        self.assertEqual(recur_gcd(10, 2), 2)
        self.assertEqual(recur_gcd(25, 10), 5)
        self.assertEqual(recur_gcd(100, 3), 3)

    def test_zero_and_negative_numbers(self):
        self.assertEqual(recur_gcd(0, 4), 4)
        self.assertEqual(recur_gcd(-4, 0), 4)
        self.assertEqual(recur_gcd(-4, -3), 1)
        self.assertEqual(recur_gcd(-4, -8), 4)
        self.assertEqual(recur_gcd(-4, -21), 7)

    def test_one(self):
        self.assertEqual(recur_gcd(1, 1), 1)
        self.assertEqual(recur_gcd(1, 2), 1)
        self.assertEqual(recur_gcd(1, 0), 1)

    def test_large_numbers(self):
        self.assertEqual(recur_gcd(123456789, 987654321), 7485873)
        self.assertEqual(recur_gcd(1234567890, 9876543210), 2147483647)
