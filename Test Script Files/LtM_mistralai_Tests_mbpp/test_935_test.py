import unittest
from mbpp_935_code import series_sum

class TestSeriesSum(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(series_sum(1), 1)
        self.assertEqual(series_sum(2), 9)
        self.assertEqual(series_sum(3), 23)

    def test_edge_input(self):
        self.assertEqual(series_sum(0), 0)
        self.assertEqual(series_sum(1000), 199500)

    def test_negative_input(self):
        self.assertEqual(series_sum(-1), -1)
        self.assertEqual(series_sum(-2), -27)
        self.assertEqual(series_sum(-3), -73)

    def test_complex_input(self):
        self.assertEqual(series_sum(10), 165)
        self.assertEqual(series_sum(20), 873)
        self.assertEqual(series_sum(30), 2220)
