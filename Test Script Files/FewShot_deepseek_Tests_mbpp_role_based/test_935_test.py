import unittest
from mbpp_935_code import series_sum

class TestSeriesSum(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertAlmostEqual(series_sum(3), 14.0/6.0)

    def test_boundary_conditions(self):
        self.assertAlmostEqual(series_sum(0), 0)
        self.assertAlmostEqual(series_sum(1), 1.0/6.0)

    def test_edge_conditions(self):
        self.assertAlmostEqual(series_sum(100), 100 * (100 + 1) * (2 * 100 + 1) / 6.0)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            series_sum('a')
        with self.assertRaises(ValueError):
            series_sum(-1)
