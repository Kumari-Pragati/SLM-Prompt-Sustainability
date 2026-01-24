import unittest
from mbpp_931_code import sum_series

class TestSumSeries(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertAlmostEqual(sum_series(5), 144.0)

    def test_boundary_conditions(self):
        self.assertAlmostEqual(sum_series(0), 0.0)
        self.assertAlmostEqual(sum_series(1), 1.0)

    def test_edge_conditions(self):
        self.assertAlmostEqual(sum_series(-1), 0.0)
        self.assertAlmostEqual(sum_series(2), 4.0)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            sum_series('a')
        with self.assertRaises(TypeError):
            sum_series(None)
