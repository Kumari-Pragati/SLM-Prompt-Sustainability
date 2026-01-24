import unittest
from mbpp_685_code import sum_Of_Primes

class TestSumOfPrimes(unittest.TestCase):

    def test_sum_of_primes_for_small_numbers(self):
        self.assertEqual(sum_Of_Primes(0), 0)
        self.assertEqual(sum_Of_Primes(1), 0)
        self.assertEqual(sum_Of_Primes(2), 2)
        self.assertEqual(sum_Of_Primes(3), 3)
        self.assertEqual(sum_Of_Primes(4), 2)
        self.assertEqual(sum_Of_Primes(5), 5)
        self.assertEqual(sum_Of_Primes(6), 3)
        self.assertEqual(sum_Of_Primes(7), 7)
        self.assertEqual(sum_Of_Primes(8), 3)
        self.assertEqual(sum_Of_Primes(9), 5)

    def test_sum_of_primes_for_large_numbers(self):
        self.assertEqual(sum_Of_Primes(100), 142913828922)
        self.assertEqual(sum_Of_Primes(1000), 1429138289220)
        self.assertEqual(sum_Of_Primes(10000), 142913828922000)
        self.assertEqual(sum_Of_Primes(100000), 142913828922000000)
        self.assertEqual(sum_Of_Primes(1000000), 142913828922000000000)
