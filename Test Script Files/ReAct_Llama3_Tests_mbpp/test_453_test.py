import unittest
from mbpp_453_code import sumofFactors

class TestSumOfFactors(unittest.TestCase):

    def test_zero(self):
        self.assertEqual(sumofFactors(0), 0)

    def test_one(self):
        self.assertEqual(sumofFactors(1), 1)

    def test_prime(self):
        self.assertEqual(sumofFactors(7), 0)

    def test_even(self):
        self.assertEqual(sumofFactors(4), 3)

    def test_perfect_square(self):
        self.assertEqual(sumofFactors(9), 2)

    def test_perfect_cube(self):
        self.assertEqual(sumofFactors(27), 3)

    def test_large_number(self):
        self.assertEqual(sumofFactors(100), 210)

    def test_edge_case(self):
        self.assertEqual(sumofFactors(2), 3)
