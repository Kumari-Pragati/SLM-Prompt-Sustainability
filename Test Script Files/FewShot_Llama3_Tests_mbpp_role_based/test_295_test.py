import unittest
from mbpp_295_code import sum_div

class TestSumDiv(unittest.TestCase):
    def test_sum_div_positive_number(self):
        self.assertEqual(sum_div(12), 18)

    def test_sum_div_zero(self):
        with self.assertRaises(ValueError):
            sum_div(0)

    def test_sum_div_negative_number(self):
        with self.assertRaises(ValueError):
            sum_div(-12)

    def test_sum_div_one(self):
        self.assertEqual(sum_div(1), 1)

    def test_sum_div_prime_number(self):
        self.assertEqual(sum_div(7), 8)

    def test_sum_div_perfect_square(self):
        self.assertEqual(sum_div(36), 60)
