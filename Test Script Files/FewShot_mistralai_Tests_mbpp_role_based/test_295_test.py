import unittest
from mbpp_295_code import sum_div

class TestSumDiv(unittest.TestCase):
    def test_positive_number(self):
        self.assertEqual(sum_div(6), 3)

    def test_negative_number(self):
        self.assertEqual(sum_div(-6), 6)

    def test_zero(self):
        self.assertEqual(sum_div(0), 0)

    def test_prime_number(self):
        self.assertEqual(sum_div(5), 1)

    def test_large_number(self):
        self.assertEqual(sum_div(1000), 25164150)
