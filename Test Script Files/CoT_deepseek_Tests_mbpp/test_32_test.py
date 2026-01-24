import unittest
from mbpp_32_code import max_Prime_Factors

class TestMaxPrimeFactors(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(max_Prime_Factors(315), 7)

    def test_small_number(self):
        self.assertEqual(max_Prime_Factors(2), 2)

    def test_large_number(self):
        self.assertEqual(max_Prime_Factors(100000000), 10000)

    def test_prime_number(self):
        self.assertEqual(max_Prime_Factors(13), 13)

    def test_negative_number(self):
        with self.assertRaises(ValueError):
            max_Prime_Factors(-10)

    def test_zero(self):
        with self.assertRaises(ValueError):
            max_Prime_Factors(0)

    def test_non_integer(self):
        with self.assertRaises(TypeError):
            max_Prime_Factors(10.5)
