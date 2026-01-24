import unittest
from mbpp_162_code import sum_series

class TestSumSeries(unittest.TestCase):
    def test_normal_input(self):
        self.assertEqual(sum_series(4), 10)
        self.assertEqual(sum_series(10), 46)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(sum_series(0), 0)
        self.assertEqual(sum_series(1), 1)
        self.assertEqual(sum_series(2), 3)
        self.assertEqual(sum_series(3), 5)

    def test_negative_input(self):
        self.assertEqual(sum_series(-1), 0)
        self.assertEqual(sum_series(-2), 0)
        self.assertEqual(sum_series(-3), 0)
