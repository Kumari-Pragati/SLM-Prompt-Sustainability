import unittest
from mbpp_45_code import get_gcd

class TestGetGCD(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(get_gcd([12, 16]), 4)
        self.assertEqual(get_gcd([20, 10]), 5)
        self.assertEqual(get_gcd([30, 45]), 5)
        self.assertEqual(get_gcd([81, 56]), 7)

    def test_zero_and_positive_numbers(self):
        self.assertEqual(get_gcd([0, 10]), 0)
        self.assertEqual(get_gcd([-10, 0]), 0)
        self.assertEqual(get_gcd([0, 20]), 0)

    def test_negative_numbers(self):
        self.assertEqual(get_gcd([-12, -16]), 4)
        self.assertEqual(get_gcd([-20, -10]), 5)
        self.assertEqual(get_gcd([-30, -45]), 5)
        self.assertEqual(get_gcd([-81, -56]), 7)

    def test_single_number(self):
        self.assertEqual(get_gcd([10]), 10)
        self.assertEqual(get_gcd([-10]), 10)
        self.assertEqual(get_gcd([0]), 0)

    def test_large_numbers(self):
        self.assertEqual(get_gcd([123456789, 987654321]), 7203)

    def test_error_handling(self):
        with self.assertRaises(TypeError):
            get_gcd([])
        with self.assertRaises(TypeError):
            get_gcd([1, 'a'])
