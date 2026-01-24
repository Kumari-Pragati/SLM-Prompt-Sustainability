import unittest
from mbpp_137_code import zero_count

class TestZeroCount(unittest.TestCase):
    def test_typical_case(self):
        self.assertAlmostEqual(zero_count([0, 1, 2, 0, 3, 4, 0]), 3/7, places=2)

    def test_edge_case_zero(self):
        self.assertAlmostEqual(zero_count([0, 0, 0, 0]), 1, places=2)

    def test_edge_case_all_nonzero(self):
        self.assertAlmostEqual(zero_count([1, 2, 3, 4, 5]), 0, places=2)

    def test_edge_case_single_zero(self):
        self.assertAlmostEqual(zero_count([0, 1, 2, 3, 4]), 1/5, places=2)

    def test_edge_case_empty_list(self):
        self.assertAlmostEqual(zero_count([]), 0, places=2)

    def test_edge_case_single_element(self):
        self.assertAlmostEqual(zero_count([0]), 1, places=2)

    def test_edge_case_all_zeros(self):
        self.assertAlmostEqual(zero_count([0, 0, 0, 0, 0]), 1, places=2)
