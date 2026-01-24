import unittest
from mbpp_687_code import divmod
from 687_code import recur_gcd

class TestRecurGCD(unittest.TestCase):

    def test_recur_gcd_positive_numbers(self):
        self.assertEqual(recur_gcd(48, 18), 6)
        self.assertEqual(recur_gcd(25, 10), 5)
        self.assertEqual(recur_gcd(30, 20), 10)
        self.assertEqual(recur_gcd(12, 18), 6)
        self.assertEqual(recur_gcd(100, 25), 5)
        self.assertEqual(recur_gcd(1000, 50), 50)

    def test_recur_gcd_zero(self):
        self.assertEqual(recur_gcd(0, 10), 10)
        self.assertEqual(recur_gcd(0, 0), 0)

    def test_recur_gcd_negative_numbers(self):
        self.assertEqual(recur_gcd(-12, -18), 6)
        self.assertEqual(recur_gcd(-25, -10), 5)
        self.assertEqual(recur_gcd(-30, -20), 10)
        self.assertEqual(recur_gcd(-12, -18), 6)
        self.assertEqual(recur_gcd(-100, -25), 5)
        self.assertEqual(recur_gcd(-1000, -50), 50)

    def test_recur_gcd_one(self):
        self.assertEqual(recur_gcd(1, 1), 1)
        self.assertEqual(recur_gcd(-1, 1), 1)
        self.assertEqual(recur_gcd(1, -1), 1)

    def test_recur_gcd_large_numbers(self):
        self.assertEqual(recur_gcd(123456789, 987654321), 749715287)
        self.assertEqual(recur_gcd(-123456789, 987654321), 749715287)
        self.assertEqual(recur_gcd(123456789, -987654321), 749715287)
