import unittest
from mbpp_491_code import sum_gp

class TestSumGP(unittest.TestCase):

    def test_simple_case(self):
        self.assertAlmostEqual(sum_gp(1, 2, 0.5), 2.5)

    def test_boundary_conditions(self):
        self.assertAlmostEqual(sum_gp(1, 1, 0), 1)
        self.assertAlmostEqual(sum_gp(1, 1, 1), 1)
        self.assertAlmostEqual(sum_gp(1, 2, 1), 0)

    def test_edge_cases(self):
        self.assertAlmostEqual(sum_gp(0, 10, 0.5), 0)
        self.assertAlmostEqual(sum_gp(1, 0, 0.5), 0)
        self.assertAlmostEqual(sum_gp(1, 10, 1), 1)

    def test_complex_cases(self):
        self.assertAlmostEqual(sum_gp(100, 5, 0.1), 112.05)
        self.assertAlmostEqual(sum_gp(1000, 10, 0.05), 1111.85)
