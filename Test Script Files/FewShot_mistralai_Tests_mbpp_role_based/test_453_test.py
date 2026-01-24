import unittest
from mbpp_453_code import sumofFactors

class TestSumofFactors(unittest.TestCase):
    def test_positive_even_number(self):
        self.assertEqual(sumofFactors(16), 31)

    def test_positive_odd_number(self):
        self.assertEqual(sumofFactors(15), 0)

    def test_zero(self):
        self.assertEqual(sumofFactors(0), 0)

    def test_negative_number(self):
        self.assertEqual(sumofFactors(-5), 0)

    def test_perfect_square(self):
        self.assertEqual(sumofFactors(169), 169)

    def test_large_number(self):
        self.assertEqual(sumofFactors(1000000), 1000000)
