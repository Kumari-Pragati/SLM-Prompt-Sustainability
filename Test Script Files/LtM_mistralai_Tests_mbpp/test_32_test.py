import unittest
from mbpp_32_code import max_Prime_Factors

class TestMaxPrimeFactors(unittest.TestCase):

    def test_simple_even(self):
        self.assertEqual(max_Prime_Factors(4), 2)
        self.assertEqual(max_Prime_Factors(8), 2)
        self.assertEqual(max_PrimeFactors(10), 2)

    def test_simple_odd(self):
        self.assertEqual(max_PrimeFactors(3), 3)
        self.assertEqual(max_PrimeFactors(5), 5)
        self.assertEqual(max_PrimeFactors(7), 7)

    def test_square_numbers(self):
        self.assertEqual(max_PrimeFactors(9), 3)
        self.assertEqual(max_PrimeFactors(25), 5)
        self.assertEqual(max_PrimeFactors(49), 7)

    def test_prime_numbers(self):
        self.assertEqual(max_PrimeFactors(11), 11)
        self.assertEqual(max_PrimeFactors(13), 13)
        self.assertEqual(max_PrimeFactors(17), 17)

    def test_composite_numbers(self):
        self.assertEqual(max_PrimeFactors(6), 2)
        self.assertEqual(max_PrimeFactors(12), 2)
        self.assertEqual(max_PrimeFactors(18), 2)
        self.assertEqual(max_PrimeFactors(20), 5)
        self.assertEqual(max_PrimeFactors(24), 2)
        self.assertEqual(max_PrimeFactors(30), 2)
        self.assertEqual(max_PrimeFactors(36), 3)

    def test_large_numbers(self):
        self.assertEqual(max_PrimeFactors(100), 5)
        self.assertEqual(max_PrimeFactors(1000), 2)
        self.assertEqual(max_PrimeFactors(10000), 2)
        self.assertEqual(max_PrimeFactors(100000), 2)
