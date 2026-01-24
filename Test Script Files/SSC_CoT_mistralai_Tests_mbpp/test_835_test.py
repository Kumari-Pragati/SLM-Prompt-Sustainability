import unittest
from mbpp_835_code import slope

class TestSlope(unittest.TestCase):
    def test_slope_normal(self):
        self.assertAlmostEqual(slope(1, 2, 3, 5), 1.0)
        self.assertAlmostEqual(slope(-1, -2, -3, -5), -1.0)

    def test_slope_edge_cases(self):
        self.assertAlmostEqual(slope(0, 0, 1, 1), 1.0)
        self.assertAlmostEqual(slope(0, 0, 0, 1), undefined)
        self.assertAlmostEqual(slope(1, 1, 0, 0), undefined)

    def test_slope_boundary_cases(self):
        self.assertAlmostEqual(slope(1e-6, 1e-6, 1, 1), 1.0)
        self.assertAlmostEqual(slope(-1e-6, -1e-6, -1, -1), -1.0)
