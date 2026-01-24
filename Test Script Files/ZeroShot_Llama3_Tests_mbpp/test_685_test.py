import unittest
from mbpp_685_code import sum_Of_Primes

class TestSumOfPrimes(unittest.TestCase):

    def test_sum_of_primes(self):
        self.assertEqual(sum_Of_Primes(10), 17)
        self.assertEqual(sum_Of_Primes(20), 78)
        self.assertEqual(sum_Of_Primes(50), 1060)
        self.assertEqual(sum_Of_Primes(100), 1060)
        self.assertEqual(sum_Of_Primes(200), 1240)
        self.assertEqual(sum_Of_Primes(500), 7450)
        self.assertEqual(sum_Of_Primes(1000), 12493)
        self.assertEqual(sum_Of_Primes(2000), 12493)
        self.assertEqual(sum_Of_Primes(5000), 45954)
        self.assertEqual(sum_Of_Primes(10000), 124933)

    def test_sum_of_primes_edge_cases(self):
        self.assertEqual(sum_Of_Primes(0), 0)
        self.assertEqual(sum_Of_Primes(1), 2)
        self.assertEqual(sum_Of_Primes(2), 2)
        self.assertEqual(sum_Of_Primes(3), 5)
        self.assertEqual(sum_Of_Primes(4), 5)
        self.assertEqual(sum_Of_Primes(5), 10)
        self.assertEqual(sum_Of_Primes(6), 10)
        self.assertEqual(sum_Of_Primes(7), 17)
        self.assertEqual(sum_Of_Primes(8), 17)
        self.assertEqual(sum_Of_Primes(9), 17)
