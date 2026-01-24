import unittest
from mbpp_55_code import tn_gp

class TestTN_GP(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertAlmostEqual(tn_gp(2, 3, 2), 8)
        self.assertAlmostEqual(tn_gp(10, 1, 2), 10)

    def test_boundary_conditions(self):
        self.assertAlmostEqual(tn_gp(1, 0, 2), 1)
        self.assertAlmostEqual(tn_gp(1, 1, 2), 1)
        self.assertAlmostEqual(tn_gp(1, 100, 2), 1)

    def test_edge_conditions(self):
        self.assertAlmostEqual(tn_gp(0, 10, 2), 0)
        self.assertAlmostEqual(tn_gp(1, 10, 0), 0)
        self.assertAlmostEqual(tn_gp(1, 10, -2), 0)

    def test_complex_cases(self):
        self.assertAlmostEqual(tn_gp(10, 5, 0.5), 3.125)
        self.assertAlmostEqual(tn_gp(10, 5, -0.5), 3.125)
