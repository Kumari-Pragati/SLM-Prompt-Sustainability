import unittest
from mbpp_685_code import sum_Of_Primes

class TestSumOfPrimes(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(sum_Of_Primes(10), 17)
        self.assertEqual(sum_Of_Primes(20), 43)
        self.assertEqual(sum_Of_Primes(30), 77)

    def test_edge(self):
        self.assertEqual(sum_Of_Primes(1), 0)
        self.assertEqual(sum_Of_Primes(2), 2)
        self.assertEqual(sum_Of_Primes(3), 2)

    def test_max(self):
        self.assertEqual(sum_Of_Primes(1000), 1060)

    def test_invalid(self):
        with self.assertRaises(TypeError):
            sum_Of_Primes("a")
