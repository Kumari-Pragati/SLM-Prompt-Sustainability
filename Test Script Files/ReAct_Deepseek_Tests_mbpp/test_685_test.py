import unittest
from mbpp_685_code import sum_Of_Primes

class TestSumOfPrimes(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(sum_Of_Primes(10), 17)

    def test_edge_case_small_number(self):
        self.assertEqual(sum_Of_Primes(2), 2)

    def test_edge_case_large_number(self):
        self.assertEqual(sum_Of_Primes(100), 1297)

    def test_edge_case_negative_number(self):
        with self.assertRaises(ValueError):
            sum_Of_Primes(-5)

    def test_edge_case_zero(self):
        self.assertEqual(sum_Of_Primes(0), 0)

    def test_edge_case_one(self):
        self.assertEqual(sum_Of_Primes(1), 0)
