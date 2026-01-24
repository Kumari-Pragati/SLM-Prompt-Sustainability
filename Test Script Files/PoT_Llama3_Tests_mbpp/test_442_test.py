import unittest
from mbpp_442_code import positive_count

class TestPositiveCount(unittest.TestCase):
    def test_typical_case(self):
        self.assertAlmostEqual(positive_count([1, 2, 3, 4, 5]), 0.5, places=2)

    def test_edge_case_all_positive(self):
        self.assertAlmostEqual(positive_count([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 1.0, places=2)

    def test_edge_case_all_negative(self):
        self.assertAlmostEqual(positive_count([-1, -2, -3, -4, -5]), 0.0, places=2)

    def test_edge_case_mixed(self):
        self.assertAlmostEqual(positive_count([-1, 2, -3, 4, -5]), 0.4, places=2)

    def test_edge_case_single_positive(self):
        self.assertAlmostEqual(positive_count([1]), 1.0, places=2)

    def test_edge_case_single_negative(self):
        self.assertAlmostEqual(positive_count([-1]), 0.0, places=2)

    def test_edge_case_empty_list(self):
        self.assertAlmostEqual(positive_count([]), 0.0, places=2)

    def test_edge_case_single_zero(self):
        self.assertAlmostEqual(positive_count([0]), 0.0, places=2)
