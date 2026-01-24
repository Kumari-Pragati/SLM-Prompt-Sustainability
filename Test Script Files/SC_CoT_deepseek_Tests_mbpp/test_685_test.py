import unittest

from mbpp_685_code import sum_Of_Primes

class TestSumOfPrimes(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(sum_Of_Primes(10), 17)

    def test_edge_case_small_number(self):
        self.assertEqual(sum_Of_Primes(2), 2)

    def test_edge_case_large_number(self):
        self.assertEqual(sum_Of_Primes(100), 1295)

    def test_special_case_prime_only(self):
        self.assertEqual(sum_Of_Primes(3), 5)

    def test_invalid_input_negative(self):
        with self.assertRaises(Exception):
            sum_Of_Primes(-10)

    def test_invalid_input_non_integer(self):
        with self.assertRaises(Exception):
            sum_Of_Primes(10.5)
