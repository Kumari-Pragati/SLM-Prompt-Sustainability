import unittest
from mbpp_687_code import recur_gcd

class TestRecurGCD(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(recur_gcd(48, 18), 6)
        self.assertEqual(recur_gcd(25, 10), 5)
        self.assertEqual(recur_gcd(12, 16), 4)

    def test_zero(self):
        self.assertEqual(recur_gcd(0, 10), 10)
        self.assertEqual(recur_gcd(10, 0), 10)

    def test_negative_numbers(self):
        self.assertEqual(recur_gcd(-12, -16), 4)
        self.assertEqual(recur_gcd(-16, -12), 4)

    def test_one(self):
        self.assertEqual(recur_gcd(1, 1), 1)

    def test_large_numbers(self):
        self.assertEqual(recur_gcd(1000000, 2000000), 2)

    def test_small_numbers(self):
        self.assertEqual(recur_gcd(1, 2), 1)
        self.assertEqual(recur_gcd(2, 1), 2)

    def test_edge_cases(self):
        self.assertEqual(recur_gcd(0, 0), 0)
        self.assertEqual(recur_gcd(1, 0), 1)
        self.assertEqual(recur_gcd(0, 1), 0)
