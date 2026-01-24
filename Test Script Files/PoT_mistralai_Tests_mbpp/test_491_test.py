import unittest
from mbpp_491_code import sum_gp

class TestSumGP(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(sum_gp(10, 5, 0.5), 30)
        self.assertEqual(sum_gp(50, 10, 0.9), 454.5454545454545)

    def test_edge_case_zero_n(self):
        self.assertAlmostEqual(sum_gp(1, 0, 0.5), 1)

    def test_edge_case_one_n(self):
        self.assertAlmostEqual(sum_gp(1, 1, 0.5), 1)

    def test_edge_case_one_r(self):
        self.assertAlmostEqual(sum_gp(1, 5, 1), 0)

    def test_corner_case_negative_a(self):
        self.assertRaises(ValueError, sum_gp, -1, 5, 0.5)

    def test_corner_case_negative_r(self):
        self.assertRaises(ValueError, sum_gp, 1, 5, -0.5)
