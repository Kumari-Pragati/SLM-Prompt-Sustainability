import unittest
from mbpp_935_code import series_sum

class TestSeriesSum(unittest.TestCase):
    def test_typical_cases(self):
        self.assertAlmostEqual(series_sum(1), 1.000)
        self.assertAlmostEqual(series_sum(2), 1.333)
        self.assertAlmostEqual(series_sum(3), 1.493)

    def test_edge_cases(self):
        self.assertAlmostEqual(series_sum(0), 0.000)

    def test_boundary_cases(self):
        self.assertAlmostEqual(series_sum(10), 142.367)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            series_sum("invalid")
