import unittest
from mbpp_685_code import sum_Of_Primes

class TestSumOfPrimes(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(sum_Of_Primes(10), 17)

    def test_small_number(self):
        self.assertEqual(sum_Of_Primes(1), 0)

    def test_large_number(self):
        self.assertEqual(sum_Of_Primes(100), 1060)

    def test_negative_number(self):
        with self.assertRaises(Exception):
            sum_Of_Primes(-10)

    def test_zero(self):
        with self.assertRaises(Exception):
            sum_Of_Primes(0)

    def test_non_integer(self):
        with self.assertRaises(Exception):
            sum_Of_Primes(10.5)

    def test_large_number_performance(self):
        # This test is for performance checking, not for correctness
        import time
        start = time.time()
        sum_Of_Primes(10000)
        end = time.time()
        self.assertLess(end - start, 1)
