import unittest
from mbpp_685_code import sum_Of_Primes

class TestSumOfPrimes(unittest.TestCase):
    def test_small_positive(self):
        self.assertEqual(sum_Of_Primes(10), 17)

    def test_large_positive(self):
        self.assertEqual(sum_Of_Primes(1000), 1060)

    def test_zero(self):
        self.assertEqual(sum_Of_Primes(0), 0)

    def test_negative(self):
        with self.assertRaises(TypeError):
            sum_Of_Primes(-1)

    def test_non_integer(self):
        with self.assertRaises(TypeError):
            sum_Of_Primes(10.5)

    def test_edge_case(self):
        self.assertEqual(sum_Of_Primes(2), 2)

    def test_edge_case2(self):
        self.assertEqual(sum_Of_Primes(1), 1)
