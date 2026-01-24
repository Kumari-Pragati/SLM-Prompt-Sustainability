import unittest
from mbpp_685_code import sum_Of_Primes

class TestSumOfPrimes(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(sum_Of_Primes(10), 2 + 3 + 5 + 7)
        self.assertEqual(sum_Of_Primes(20), 2 + 3 + 5 + 7 + 11 + 13 + 17)
        self.assertEqual(sum_Of_Primes(100), 2 + 3 + 5 + 7 + 11 + 13 + 17 + 19 + 23 + 29 + 31 + 37 + 41 + 43 + 47 + 53 + 59 + 61 + 67 + 71 + 73 + 79 + 83 + 89 + 97)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(sum_Of_Primes(1), 1)
        self.assertEqual(sum_Of_Primes(2), 2)
        self.assertEqual(sum_Of_Primes(0), 0)
        self.assertEqual(sum_Of_Primes(1000), sum(p for p in range(2, 1001) if p % 2 == 0))  # Checking only even numbers since 2 is the only even prime number
        self.assertEqual(sum_Of_Primes(10000), sum(p for p in range(2, 10001) if p % 2 == 0))  # Checking only even numbers
