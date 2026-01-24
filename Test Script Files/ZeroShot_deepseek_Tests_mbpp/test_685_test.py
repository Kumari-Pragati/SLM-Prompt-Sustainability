import unittest
from mbpp_685_code import sum_Of_Primes

class TestSumOfPrimes(unittest.TestCase):

    def test_sum_of_primes_with_small_number(self):
        self.assertEqual(sum_Of_Primes(10), 17)

    def test_sum_of_primes_with_large_number(self):
        self.assertEqual(sum_Of_Primes(100), 1060)

    def test_sum_of_primes_with_negative_number(self):
        self.assertEqual(sum_Of_Primes(-10), 0)

    def test_sum_of_primes_with_zero(self):
        self.assertEqual(sum_Of_Primes(0), 0)

    def test_sum_of_primes_with_one(self):
        self.assertEqual(sum_Of_Primes(1), 0)
