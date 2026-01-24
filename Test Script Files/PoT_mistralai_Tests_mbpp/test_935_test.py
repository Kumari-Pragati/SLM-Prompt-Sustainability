import unittest
from mbpp_935_code import series_sum

class TestSeriesSum(unittest.TestCase):
    def test_typical_cases(self):
        self.assertEqual(series_sum(1), 1)
        self.assertEqual(series_sum(2), 9 / 2)
        self.assertEqual(series_sum(3), 13)
        self.assertEqual(series_sum(4), 30 / 2)
        self.assertEqual(series_sum(5), 35 / 2)

    def test_edge_and_boundary_cases(self):
        self.assertEqual(series_sum(0), 0)
        self.assertEqual(series_sum(100), 19950)
