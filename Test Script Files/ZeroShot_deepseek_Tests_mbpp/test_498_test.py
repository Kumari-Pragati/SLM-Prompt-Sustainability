import unittest
from mbpp_498_code import gcd

class TestGCD(unittest.TestCase):

    def test_gcd_positive_numbers(self):
        self.assertEqual(gcd(48, 18), 6)
        self.assertEqual(gcd(101, 103), 1)
        self.assertEqual(gcd(100, 200), 100)

    def test_gcd_negative_numbers(self):
        self.assertEqual(gcd(-48, -18), 6)
        self.assertEqual(gcd(-101, -103), 1)
        self.assertEqual(gcd(-100, -200), 100)

    def test_gcd_mixed_numbers(self):
        self.assertEqual(gcd(-48, 18), 6)
        self.assertEqual(gcd(101, -103), 1)
        self.assertEqual(gcd(-100, 200), 100)

    def test_gcd_zero(self):
        self.assertEqual(gcd(0, 18), 18)
        self.assertEqual(gcd(101, 0), 101)
        self.assertEqual(gcd(0, 0), 0)

    def test_gcd_equal_numbers(self):
        self.assertEqual(gcd(100, 100), 100)
        self.assertEqual(gcd(0, 0), 0)
