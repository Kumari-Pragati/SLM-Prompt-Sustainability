import unittest
from mbpp_442_code import positive_count

class TestPositiveCount(unittest.TestCase):

    def test_typical_case(self):
        self.assertAlmostEqual(positive_count([1, 2, 3, 4, 5]), 1.0)

    def test_edge_case_empty_list(self):
        self.assertAlmostEqual(positive_count([]), 0.0)

    def test_edge_case_all_negative(self):
        self.assertAlmostEqual(positive_count([-1, -2, -3, -4, -5]), 0.0)

    def test_edge_case_single_zero(self):
        self.assertAlmostEqual(positive_count([0, 1, 2, 3, 4, 5]), 0.5)

    def test_edge_case_single_positive_and_negative(self):
        self.assertAlmostEqual(positive_count([-1, 1]), 0.5)
