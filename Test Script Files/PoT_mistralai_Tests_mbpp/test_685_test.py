import unittest
from mbpp_685_code import sum_Of_Primes

class TestSumOfPrimes(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(sum_Of_Primes(10), 17)
        self.assertEqual(sum_Of_Primes(20), 91)
        self.assertEqual(sum_Of_Primes(100), 3054)

    def test_edge_cases(self):
        self.assertEqual(sum_Of_Primes(1), 0)
        self.assertEqual(sum_Of_Primes(2), 2)
        self.assertEqual(sum_Of_Primes(3), 2)
        self.assertEqual(sum_Of_Primes(4), 5)

    def test_boundary_cases(self):
        self.assertEqual(sum_Of_Primes(0), 0)
        self.assertEqual(sum_Of_Primes(5000), 1491668)
