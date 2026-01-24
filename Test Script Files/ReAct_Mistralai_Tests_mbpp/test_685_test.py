import unittest
from mbpp_685_code import sum_Of_Primes

class TestSumOfPrimes(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(sum_Of_Primes(0), 0)

    def test_single_prime(self):
        self.assertEqual(sum_Of_Primes(2), 2)
        self.assertEqual(sum_Of_Primes(3), 3)
        self.assertEqual(sum_Of_Primes(5), 5)

    def test_small_numbers(self):
        self.assertEqual(sum_Of_Primes(6), 3)
        self.assertEqual(sum_Of_Primes(10), 23)
        self.assertEqual(sum_Of_Primes(15), 38)

    def test_large_numbers(self):
        self.assertEqual(sum_Of_Primes(100), 142913828922)
        self.assertEqual(sum_Of_Primes(1000), 1429138289220026047)

    def test_prime_powers(self):
        self.assertEqual(sum_Of_Primes(4), 3)
        self.assertEqual(sum_Of_Primes(9), 15)
        self.assertEqual(sum_Of_Primes(25), 151)

    def test_large_prime_powers(self):
        self.assertEqual(sum_Of_Primes(16), 31)
        self.assertEqual(sum_Of_Primes(28), 101)
        self.assertEqual(sum_Of_Primes(64), 1641)

    def test_prime_squares(self):
        self.assertEqual(sum_Of_Primes(16), 31)
        self.assertEqual(sum_Of_Primes(29), 31)
        self.assertEqual(sum_Of_Primes(44), 101)

    def test_large_prime_squares(self):
        self.assertEqual(sum_Of_Primes(65), 1641)
        self.assertEqual(sum_Of_Primes(101), 1641)
        self.assertEqual(sum_Of_Primes(169), 3101)

    def test_prime_cubes(self):
        self.assertEqual(sum_Of_Primes(125), 1641)
        self.assertEqual(sum_Of_Primes(216), 3101)
        self.assertEqual(sum_Of_Primes(343), 10101)

    def test_large_prime_cubes(self):
        self.assertEqual(sum_Of_Primes(1296), 10101)
        self.assertEqual(sum_Of_Primes(2197), 10101)
        self.assertEqual(sum_Of_Primes(3436), 1010101)

    def test_negative_numbers(self):
        self.assertRaises(ValueError, sum_Of_Primes, -1)
