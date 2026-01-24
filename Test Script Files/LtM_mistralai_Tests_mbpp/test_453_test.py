import unittest
from mbpp_453_code import sumofFactors

class TestSumOfFactors(unittest.TestCase):
    def test_simple_even_number(self):
        self.assertEqual(sumofFactors(4), 8)
        self.assertEqual(sumofFactors(12), 108)

    def test_edge_cases(self):
        self.assertEqual(sumofFactors(0), 0)
        self.assertEqual(sumofFactors(1), 1)
        self.assertEqual(sumofFactors(2), 2)
        self.assertEqual(sumofFactors(3), 0)

    def test_square_numbers(self):
        self.assertEqual(sumofFactors(4), 8)
        self.assertEqual(sumofFactors(9), 36)
        self.assertEqual(sumofFactors(16), 120)

    def test_prime_numbers(self):
        self.assertEqual(sumofFactors(5), 6)
        self.assertEqual(sumofFactors(7), 7)

    def test_composite_numbers(self):
        self.assertEqual(sumofFactors(10), 40)
        self.assertEqual(sumofFactors(15), 120)
        self.assertEqual(sumofFactors(20), 240)
