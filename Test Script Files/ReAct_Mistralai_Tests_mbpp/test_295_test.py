import unittest
from mbpp_295_code import sum_div

class TestSumDiv(unittest.TestCase):

    def test_positive_numbers(self):
        """Test sum_div function with positive numbers"""
        self.assertEqual(sum_div(4), 3)
        self.assertEqual(sum_div(6), 3)
        self.assertEqual(sum_div(28), 14)

    def test_zero(self):
        """Test sum_div function with zero"""
        self.assertEqual(sum_div(0), 0)

    def test_negative_numbers(self):
        """Test sum_div function with negative numbers"""
        self.assertEqual(sum_div(-4), 4)
        self.assertEqual(sum_div(-20), 10)

    def test_prime_numbers(self):
        """Test sum_div function with prime numbers"""
        self.assertEqual(sum_div(2), 2)
        self.assertEqual(sum_div(5), 1)
        self.assertEqual(sum_div(11), 1)

    def test_edge_cases(self):
        """Test sum_div function with edge cases"""
        self.assertEqual(sum_div(1), 1)
        self.assertEqual(sum_div(2), 2)
