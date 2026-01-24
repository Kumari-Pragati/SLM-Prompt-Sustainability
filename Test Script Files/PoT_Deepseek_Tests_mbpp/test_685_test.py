import unittest
from mbpp_685_code import sum_Of_Primes

class TestSumOfPrimes(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(sum_Of_Primes(10), 17)
        self.assertEqual(sum_Of_Primes(20), 77)

    def test_edge_cases(self):
        self.assertEqual(sum_Of_Primes(0), 0)
        self.assertEqual(sum_Of_Primes(1), 0)

    def test_boundary_cases(self):
        self.assertEqual(sum_Of_Primes(2), 2)
        self.assertEqual(sum_Of_Primes(3), 5)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            sum_Of_Primes("10")
        with self.assertRaises(ValueError):
            sum_Of_Primes(-10)
