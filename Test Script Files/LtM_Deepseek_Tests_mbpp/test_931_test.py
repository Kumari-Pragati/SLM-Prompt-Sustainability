import unittest
from mbpp_931_code import sum_series

class TestSumSeries(unittest.TestCase):

    def test_simple_input(self):
        self.assertAlmostEqual(sum_series(1), 1.0)

    def test_boundary_conditions(self):
        self.assertAlmostEqual(sum_series(0), 0.0)
        self.assertAlmostEqual(sum_series(100), 338350.0)

    def test_edge_cases(self):
        self.assertAlmostEqual(sum_series(-1), 0.0)
        self.assertAlmostEqual(sum_series(1.5), 2.25)

    def test_complex_cases(self):
        self.assertAlmostEqual(sum_series(2), 4.0)
        self.assertAlmostEqual(sum_series(3), 14.0)
