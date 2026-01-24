import unittest
from mbpp_530_code import negative_count

class TestNegativeCount(unittest.TestCase):
    def test_typical_case(self):
        self.assertAlmostEqual(negative_count([-1, 0, 1, -2]), 0.5)

    def test_edge_case_all_negative(self):
        self.assertAlmostEqual(negative_count([-10, -20, -30]), 1.0)

    def test_edge_case_all_positive(self):
        self.assertAlmostEqual(negative_count([1, 2, 3]), 0.0)

    def test_edge_case_single_negative(self):
        self.assertAlmostEqual(negative_count([0, -1, 0]), 0.33333333333333336)

    def test_corner_case_empty_list(self):
        self.assertAlmostEqual(negative_count([]), 0.0)

    def test_corner_case_single_zero(self):
        self.assertAlmostEqual(negative_count([0]), 0.0)
