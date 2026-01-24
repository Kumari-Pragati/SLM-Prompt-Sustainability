import unittest
from mbpp_687_code import recur_gcd

class TestGCD(unittest.TestCase):

    def test_gcd_positive_numbers(self):
        self.assertEqual(recur_gcd(48, 18), 6)
        self.assertEqual(recur_gcd(101, 103), 1)
        self.assertEqual(recur_gcd(36, 24), 12)

    def test_gcd_negative_numbers(self):
        self.assertEqual(recur_gcd(-48, -18), 6)
        self.assertEqual(recur_gcd(-101, -103), 1)
        self.assertEqual(recur_gcd(-36, -24), 12)

    def test_gcd_mixed_numbers(self):
        self.assertEqual(recur_gcd(-48, 18), 6)
        self.assertEqual(recur_gcd(101, -103), 1)
        self.assertEqual(recur_gcd(-36, 24), 12)

    def test_gcd_zero(self):
        self.assertEqual(recur_gcd(0, 18), 18)
        self.assertEqual(recur_gcd(101, 0), 101)
        self.assertEqual(recur_gcd(0, 0), 0)

    def test_gcd_one(self):
        self.assertEqual(recur_gcd(1, 18), 1)
        self.assertEqual(recur_gcd(101, 1), 1)
        self.assertEqual(recur_gcd(1, 0), 1)
