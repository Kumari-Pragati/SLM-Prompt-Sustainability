import unittest
from mbpp_32_code import max_Prime_Factors

class TestMaxPrimeFactors(unittest.TestCase):
    def test_prime_number(self):
        self.assertEqual(max_Prime_Factors(29), 29)

    def test_composite_number(self):
        self.assertEqual(max_Prime_Factors(36), 6)

    def test_large_prime_number(self):
        self.assertEqual(max_Prime_Factors(1000003), 1000003)

    def test_small_composite_number(self):
        self.assertEqual(max_Prime_Factors(4), 2)

    def test_zero(self):
        self.assertEqual(max_PrimeFactors(0), 0)

    def test_negative_number(self):
        self.assertEqual(max_PrimeFactors(-1), -1)

    def test_large_composite_number(self):
        self.assertEqual(max_PrimeFactors(9999998), 2)
