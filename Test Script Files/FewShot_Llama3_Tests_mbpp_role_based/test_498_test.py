import unittest
from mbpp_498_code import gcd

class TestGcd(unittest.TestCase):
    def test_gcd_of_two_numbers(self):
        self.assertEqual(gcd(12, 15), 3)

    def test_gcd_of_one_number(self):
        self.assertEqual(gcd(12, 12), 12)

    def test_gcd_of_zero(self):
        self.assertEqual(gcd(0, 0), 1)

    def test_gcd_of_non_integer(self):
        with self.assertRaises(TypeError):
            gcd(12.5, 15)

    def test_gcd_of_negative_numbers(self):
        self.assertEqual(gcd(-12, 15), 3)

    def test_gcd_of_negative_and_positive_numbers(self):
        self.assertEqual(gcd(-12, 15), 3)
