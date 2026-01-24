import unittest
from mbpp_432_code import median_trapezium

class TestMedianTrapezium(unittest.TestCase):

    def test_normal_inputs(self):
        self.assertAlmostEqual(median_trapezium(2, 3, 1), 2.5)
        self.assertAlmostEqual(median_trapezium(4, 1, 2), 2.5)
        self.assertAlmostEqual(median_trapezium(0.5, 1.5, 1), 1)

    def test_edge_and_boundary_conditions(self):
        self.assertAlmostEqual(median_trapezium(0, 0, 1), 0)
        self.assertAlmostEqual(median_trapezium(0, 1, 0), 0.5)
        self.assertAlmostEqual(median_trapezium(1, 0, 0), 0.5)
        self.assertAlmostEqual(median_trapezium(1, 1, 0), 1)
