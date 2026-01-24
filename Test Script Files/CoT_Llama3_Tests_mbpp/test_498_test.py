import unittest
from mbpp_498_code import gcd

class TestGCD(unittest.TestCase):
    def test_gcd_of_two_numbers(self):
        self.assertEqual(gcd(48, 18), 6)

    def test_gcd_of_prime_numbers(self):
        self.assertEqual(gcd(23, 17), 1)

    def test_gcd_of_perfect_numbers(self):
        self.assertEqual(gcd(36, 36), 36)

    def test_gcd_of_one_number(self):
        self.assertEqual(gcd(12, 0), 12)

    def test_gcd_of_zero(self):
        with self.assertRaises(ZeroDivisionError):
            gcd(0, 0)

    def test_gcd_of_negative_numbers(self):
        self.assertEqual(gcd(-12, 15), 3)

    def test_gcd_of_large_numbers(self):
        self.assertEqual(gcd(123456, 7654321), 3)
