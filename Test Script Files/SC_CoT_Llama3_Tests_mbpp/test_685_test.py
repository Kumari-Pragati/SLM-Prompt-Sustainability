import unittest
from mbpp_685_code import sum_Of_Primes

class TestSumOfPrimes(unittest.TestCase):
    def test_sum_of_primes_for_small_numbers(self):
        self.assertEqual(sum_Of_Primes(10), 17)

    def test_sum_of_primes_for_large_numbers(self):
        self.assertEqual(sum_Of_Primes(1000), 1060)

    def test_sum_of_primes_for_edge_cases(self):
        self.assertEqual(sum_Of_Primes(2), 2)
        self.assertEqual(sum_Of_Primes(3), 2)

    def test_sum_of_primes_for_zero(self):
        self.assertEqual(sum_Of_Primes(0), 0)

    def test_sum_of_primes_for_negative_numbers(self):
        with self.assertRaises(TypeError):
            sum_Of_Primes(-1)

    def test_sum_of_primes_for_non_integer(self):
        with self.assertRaises(TypeError):
            sum_Of_Primes(10.5)
