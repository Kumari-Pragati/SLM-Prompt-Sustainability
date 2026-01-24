import unittest
from mbpp_738_code import geometric_sum

class TestGeometricSum(unittest.TestCase):

    def test_typical_case(self):
        self.assertAlmostEqual(geometric_sum(3), 0.125)

    def test_edge_case_n_zero(self):
        self.assertAlmostEqual(geometric_sum(0), 1)

    def test_edge_case_n_negative(self):
        self.assertEqual(geometric_sum(-1), 0)

    def test_edge_case_n_one(self):
        self.assertAlmostEqual(geometric_sum(1), 0.5)

    def test_edge_case_n_large(self):
        self.assertAlmostEqual(geometric_sum(10), 0.0009765625)

    def test_edge_case_n_zero_recursive(self):
        self.assertEqual(geometric_sum(0), 1)

    def test_edge_case_n_negative_recursive(self):
        self.assertEqual(geometric_sum(-1), 0)

    def test_edge_case_n_one_recursive(self):
        self.assertAlmostEqual(geometric_sum(1), 0.5)

    def test_edge_case_n_large_recursive(self):
        self.assertAlmostEqual(geometric_sum(10), 0.0009765625)
