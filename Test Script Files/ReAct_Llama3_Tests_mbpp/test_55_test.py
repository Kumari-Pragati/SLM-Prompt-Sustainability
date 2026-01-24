import unittest
from mbpp_55_code import tn_gp

class TestTnGp(unittest.TestCase):

    def test_typical_case(self):
        self.assertAlmostEqual(tn_gp(10, 5, 0.05), 10 * math.pow(0.05, 4))

    def test_edge_case_n_zero(self):
        self.assertEqual(tn_gp(10, 0, 0.05), 0)

    def test_edge_case_r_zero(self):
        self.assertEqual(tn_gp(10, 5, 0), 0)

    def test_edge_case_a_zero(self):
        self.assertEqual(tn_gp(0, 5, 0.05), 0)

    def test_edge_case_n_one(self):
        self.assertAlmostEqual(tn_gp(10, 1, 0.05), 10 * 0.05)

    def test_edge_case_r_one(self):
        self.assertEqual(tn_gp(10, 5, 1), 10)

    def test_edge_case_a_one(self):
        self.assertEqual(tn_gp(1, 5, 0.05), 1)

    def test_edge_case_n_negative(self):
        with self.assertRaises(ValueError):
            tn_gp(10, -5, 0.05)

    def test_edge_case_r_negative(self):
        with self.assertRaises(ValueError):
            tn_gp(10, 5, -0.05)

    def test_edge_case_a_negative(self):
        with self.assertRaises(ValueError):
            tn_gp(-10, 5, 0.05)
