import unittest
from mbpp_935_code import series_sum

class TestSeriesSum(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertAlmostEqual(series_sum(1), 1.000)
        self.assertAlmostEqual(series_sum(2), 1.333)
        self.assertAlmostEqual(series_sum(3), 1.493)

    def test_edge_conditions(self):
        self.assertAlmostEqual(series_sum(0), 0.000)
        self.assertAlmostEqual(series_sum(10), 142.366)

    def test_boundary_conditions(self):
        self.assertAlmostEqual(series_sum(100), 166666.666)

    def test_complex_cases(self):
        self.assertAlmostEqual(series_sum(5), 2.275)
        self.assertAlmostEqual(series_sum(7), 3.708)
