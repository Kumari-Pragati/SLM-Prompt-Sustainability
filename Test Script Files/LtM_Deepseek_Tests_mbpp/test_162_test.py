import unittest
from mbpp_162_code import sum_series

class TestSumSeries(unittest.TestCase):

    def test_simple_positive_numbers(self):
        self.assertEqual(sum_series(1), 1)
        self.assertEqual(sum_series(3), 6)
        self.assertEqual(sum_series(5), 15)

    def test_boundary_conditions(self):
        self.assertEqual(sum_series(0), 0)
        self.assertEqual(sum_series(-1), 0)
        self.assertEqual(sum_series(2), 2)

    def test_complex_cases(self):
        self.assertEqual(sum_series(4), 10)
        self.assertEqual(sum_series(6), 21)
