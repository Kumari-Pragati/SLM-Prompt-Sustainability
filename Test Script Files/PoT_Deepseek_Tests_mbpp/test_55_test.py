import unittest
from mbpp_55_code import tn_gp

class TestTnGp(unittest.TestCase):

    def test_typical_case(self):
        self.assertAlmostEqual(tn_gp(2, 3, 2), 4.0)

    def test_edge_case_n_equals_1(self):
        self.assertAlmostEqual(tn_gp(2, 1, 2), 2.0)

    def test_boundary_case_r_equals_1(self):
        self.assertAlmostEqual(tn_gp(2, 3, 1), 2.0)
        self.assertAlmostEqual(tn_gp(2, 1, 1), 2.0)

    def test_corner_case_r_equals_0(self):
        self.assertAlmostEqual(tn_gp(2, 3, 0), 0.0)

    def test_invalid_input_n_less_than_1(self):
        with self.assertRaises(Exception):
            tn_gp(2, 0, 2)

    def test_invalid_input_negative_r(self):
        with self.assertRaises(Exception):
            tn_gp(2, 3, -2)
