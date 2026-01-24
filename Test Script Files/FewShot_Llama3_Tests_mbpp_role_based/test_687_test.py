import unittest
from mbpp_687_code import recur_gcd

class TestRecGCD(unittest.TestCase):
    def test_gcd_of_two_numbers(self):
        self.assertEqual(recur_gcd(12, 15), 3)

    def test_gcd_of_one_number(self):
        self.assertEqual(recur_gcd(12, 0), 12)

    def test_gcd_of_zero(self):
        self.assertEqual(recur_gcd(0, 0), 0)

    def test_gcd_of_one(self):
        self.assertEqual(recur_gcd(1, 1), 1)

    def test_gcd_of_negative_numbers(self):
        self.assertEqual(recur_gcd(-12, -15), 3)

    def test_gcd_of_mixed_sign_numbers(self):
        self.assertEqual(recur_gcd(12, -15), 3)
