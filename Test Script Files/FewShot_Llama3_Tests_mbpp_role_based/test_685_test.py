import unittest
from mbpp_685_code import sum_Of_Primes

class TestSumOfPrimes(unittest.TestCase):
    def test_sum_of_primes_for_small_numbers(self):
        self.assertEqual(sum_Of_Primes(10), 17)

    def test_sum_of_primes_for_large_numbers(self):
        self.assertEqual(sum_Of_Primes(100), 1060)

    def test_sum_of_primes_for_edge_case(self):
        self.assertEqual(sum_Of_Primes(1), 1)

    def test_sum_of_primes_for_zero(self):
        with self.assertRaises(TypeError):
            sum_Of_Primes(0)

    def test_sum_of_primes_for_negative_numbers(self):
        with self.assertRaises(TypeError):
            sum_Of_Primes(-1)
