import unittest
from mbpp_453_code import sumofFactors

class TestSumOfFactors(unittest.TestCase):
    def test_even_perfect_square(self):
        self.assertEqual(sumofFactors(4), 8)

    def test_even_non_perfect_square(self):
        self.assertEqual(sumofFactors(18), 120)

    def test_odd_number(self):
        self.assertEqual(sumofFactors(5), 0)

    def test_zero(self):
        self.assertEqual(sumofFactors(0), 0)

    def test_negative_number(self):
        self.assertEqual(sumofFactors(-1), 0)

    def test_large_number(self):
        self.assertEqual(sumofFactors(1000001), 1000001)

    def test_prime_number(self):
        self.assertEqual(sumofFactors(3), 3)
