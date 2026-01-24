import unittest
from mbpp_491_code import sum_gp

class TestSumGP(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertAlmostEqual(sum_gp(1, 5, 0.5), 6.0)

    def test_boundary_conditions(self):
        self.assertAlmostEqual(sum_gp(1, 1, 0.5), 1.0)
        self.assertAlmostEqual(sum_gp(1, 100, 0.5), 100.0)

    def test_edge_conditions(self):
        self.assertAlmostEqual(sum_gp(1, 0, 0.5), 0.0)
        self.assertAlmostEqual(sum_gp(1, 1000, 1), 1000.0)

    def test_invalid_inputs(self):
        with self.assertRaises(ValueError):
            sum_gp(1, -5, 0.5)
        with self.assertRaises(ValueError):
            sum_gp(1, 5, 1.5)
