import unittest
from mbpp_685_code import sum_Of_Primes

class TestSumOfPrimes(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(sum_Of_Primes(10), 2 + 3 + 5 + 7)

    def test_small_input(self):
        self.assertEqual(sum_Of_Primes(1), 2)
        self.assertEqual(sum_Of_Primes(2), 2)
        self.assertEqual(sum_Of_Primes(3), 3)

    def test_large_input(self):
        self.assertEqual(sum_Of_Primes(100), 1 + 3 + 5 + 7 + 11 + 13 + 17 + 19 + 23 + 29 + 31 + 37 + 41 + 43 + 47 + 53 + 59 + 61 + 67 + 71 + 73 + 79 + 83 + 89 + 97)

    def test_edge_cases(self):
        self.assertEqual(sum_Of_Primes(0), 0)
        self.assertEqual(sum_Of_Primes(1), 2)
        self.assertEqual(sum_Of_Primes(2), 2)
        self.assertEqual(sum_Of_Primes(3), 3)
        self.assertEqual(sum_Of_Primes(4), 2)
        self.assertEqual(sum_Of_Primes(5), 2 + 3)
