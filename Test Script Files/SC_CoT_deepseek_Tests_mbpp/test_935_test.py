import unittest
from mbpp_935_code import series_sum

class TestSeriesSum(unittest.TestCase):
    def test_typical_case(self):
        self.assertAlmostEqual(series_sum(3), 14.0/6.0)

    def test_boundary_case(self):
        self.assertAlmostEqual(series_sum(0), 0.0)

    def test_edge_case(self):
        self.assertAlmostEqual(series_sum(1), 1.0/6.0)

    def test_large_number(self):
        self.assertAlmostEqual(series_sum(10), 140.0/6.0)

    def test_negative_number(self):
        with self.assertRaises(ValueError):
            series_sum(-1)

    def test_non_integer_number(self):
        with self.assertRaises(TypeError):
            series_sum(1.5)
