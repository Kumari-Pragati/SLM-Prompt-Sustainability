import unittest
from mbpp_687_code import recur_gcd

class TestRecurGcd(unittest.TestCase):

    def test_gcd_of_two_small_numbers(self):
        self.assertEqual(recur_gcd(12, 15), 3)

    def test_gcd_of_two_large_numbers(self):
        self.assertEqual(recur_gcd(123456, 789012), 3)

    def test_gcd_of_one_zero(self):
        self.assertEqual(recur_gcd(0, 15), 15)

    def test_gcd_of_one_one(self):
        self.assertEqual(recur_gcd(1, 15), 1)

    def test_gcd_of_two_zeros(self):
        self.assertEqual(recur_gcd(0, 0), 0)

    def test_gcd_of_two_negative_numbers(self):
        self.assertEqual(recur_gcd(-12, -15), 3)

    def test_gcd_of_two_mixed_sign_numbers(self):
        self.assertEqual(recur_gcd(12, -15), 3)
