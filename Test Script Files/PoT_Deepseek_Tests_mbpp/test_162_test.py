import unittest
from mbpp_162_code import sum_series

class TestSumSeries(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(sum_series(1), 1)
        self.assertEqual(sum_series(3), 6)
        self.assertEqual(sum_series(5), 14)

    def test_edge_cases(self):
        self.assertEqual(sum_series(0), 0)
        self.assertEqual(sum_series(-1), 0)
        self.assertEqual(sum_series(-5), 0)

    def test_corner_cases(self):
        self.assertEqual(sum_series(2), 2)
        self.assertEqual(sum_series(4), 10)
