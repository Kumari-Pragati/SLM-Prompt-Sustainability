import unittest
from mbpp_32_code import max_Prime_Factors

class TestMaxPrimeFactors(unittest.TestCase):
    def test_max_prime_factors_of_10(self):
        self.assertEqual(max_Prime_Factors(10), 2)

    def test_max_prime_factors_of_15(self):
        self.assertEqual(max_Prime_Factors(15), 3)

    def test_max_prime_factors_of_24(self):
        self.assertEqual(max_Prime_Factors(24), 3)

    def test_max_prime_factors_of_37(self):
        self.assertEqual(max_Prime_Factors(37), 37)

    def test_max_prime_factors_of_48(self):
        self.assertEqual(max_Prime_Factors(48), 3)

    def test_max_prime_factors_of_50(self):
        self.assertEqual(max_Prime_Factors(50), 5)

    def test_max_prime_factors_of_100(self):
        self.assertEqual(max_Prime_Factors(100), 5)

    def test_max_prime_factors_of_1(self):
        self.assertEqual(max_Prime_Factors(1), 1)

    def test_max_prime_factors_of_0(self):
        with self.assertRaises(ValueError):
            max_Prime_Factors(0)
