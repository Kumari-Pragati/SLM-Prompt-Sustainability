import unittest
from mbpp_685_code import sum_Of_Primes

class TestSumOfPrimes(unittest.TestCase):
    def test_sum_of_primes_with_small_input(self):
        self.assertEqual(sum_Of_Primes(10), 25)

    def test_sum_of_primes_with_large_input(self):
        self.assertEqual(sum_Of_Primes(100), 142913828922)

    def test_sum_of_primes_with_prime_input(self):
        self.assertEqual(sum_Of_Primes(23), 23)

    def test_sum_of_primes_with_composite_input(self):
        self.assertEqual(sum_Of_Primes(15), 23)

    def test_sum_of_primes_with_zero(self):
        self.assertEqual(sum_Of_Primes(0), 0)

    def test_sum_of_primes_with_negative_input(self):
        self.assertRaises(ValueError, sum_Of_Primes, -1)
