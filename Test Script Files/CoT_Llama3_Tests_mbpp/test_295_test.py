import unittest
from mbpp_295_code import sum_div

class TestSumDiv(unittest.TestCase):

    def test_sum_div_positive(self):
        self.assertEqual(sum_div(12), 18)

    def test_sum_div_negative(self):
        with self.assertRaises(TypeError):
            sum_div(-12)

    def test_sum_div_zero(self):
        self.assertEqual(sum_div(0), 1)

    def test_sum_div_one(self):
        self.assertEqual(sum_div(1), 1)

    def test_sum_div_prime(self):
        self.assertEqual(sum_div(7), 8)

    def test_sum_div_composite(self):
        self.assertEqual(sum_div(36), 60)

    def test_sum_div_edge(self):
        self.assertEqual(sum_div(2), 2)

    def test_sum_div_edge2(self):
        self.assertEqual(sum_div(3), 4)
