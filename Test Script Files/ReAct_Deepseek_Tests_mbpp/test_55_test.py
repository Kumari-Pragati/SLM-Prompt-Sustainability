import unittest
from mbpp_55_code import tn_gp

class TestTN_GP(unittest.TestCase):

    def test_typical_case(self):
        self.assertAlmostEqual(tn_gp(2, 3, 2), 4.0)

    def test_boundary_case_zero_a(self):
        self.assertAlmostEqual(tn_gp(0, 3, 2), 0.0)

    def test_boundary_case_zero_r(self):
        self.assertAlmostEqual(tn_gp(2, 3, 0), 0.0)

    def test_boundary_case_n_equals_1(self):
        self.assertAlmostEqual(tn_gp(2, 1, 2), 2.0)

    def test_edge_case_negative_a(self):
        self.assertAlmostEqual(tn_gp(-2, 3, 2), -4.0)

    def test_edge_case_negative_r(self):
        self.assertAlmostEqual(tn_gp(2, 3, -2), -4.0)

    def test_edge_case_large_n(self):
        self.assertAlmostEqual(tn_gp(2, 10, 2), 512.0)

    def test_edge_case_large_a(self):
        self.assertAlmostEqual(tn_gp(1000, 3, 2), 8000.0)
