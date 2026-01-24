import unittest
from mbpp_530_code import negative_count

class TestNegativeCount(unittest.TestCase):
    def test_simple_positive(self):
        self.assertAlmostEqual(negative_count([1, 2, 3]), 0.0)

    def test_simple_negative(self):
        self.assertAlmostEqual(negative_count([-1, -2, -3]), 1.0)

    def test_single_negative(self):
        self.assertAlmostEqual(negative_count([0, -1]), 0.5)

    def test_edge_cases_min(self):
        self.assertAlmostEqual(negative_count([-1000000]), 1.0)

    def test_edge_cases_max(self):
        self.assertAlmostEqual(negative_count([1000000]), 0.0)

    def test_empty_list(self):
        self.assertAlmostEqual(negative_count([]), 0.0)

    def test_complex_case_1(self):
        self.assertAlmostEqual(negative_count([-1, 1, -2, 3, -4, 5]), 0.6)
