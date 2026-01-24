import unittest
from mbpp_32_code import max_Prime_Factors

class TestMaxPrimeFactors(unittest.TestCase):

    def test_simple_positive_number(self):
        self.assertEqual(max_Prime_Factors(25), 5)

    def test_even_number(self):
        self.assertEqual(max_Prime_Factors(12), 2)

    def test_prime_number(self):
        self.assertEqual(max_Prime_Factors(7), 7)

    def test_square_number(self):
        self.assertEqual(max_Prime_Factors(9), 3)

    def test_large_number(self):
        self.assertEqual(max_Prime_Factors(1000000007), 1000000007)

    def test_small_number(self):
        self.assertEqual(max_Prime_Factors(1), 1)

    def test_zero(self):
        with self.assertRaises(ValueError):
            max_Prime_Factors(0)

    def test_negative_number(self):
        with self.assertRaises(ValueError):
            max_Prime_Factors(-1)
