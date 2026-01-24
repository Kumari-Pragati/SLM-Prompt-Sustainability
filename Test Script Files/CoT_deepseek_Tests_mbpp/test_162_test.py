import unittest
from mbpp_162_code import sum_series

class TestSumSeries(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(sum_series(5), 14)

    def test_boundary_conditions(self):
        self.assertEqual(sum_series(0), 0)
        self.assertEqual(sum_series(1), 1)

    def test_negative_numbers(self):
        self.assertEqual(sum_series(-5), 0)

    def test_large_numbers(self):
        self.assertEqual(sum_series(10), 55)
