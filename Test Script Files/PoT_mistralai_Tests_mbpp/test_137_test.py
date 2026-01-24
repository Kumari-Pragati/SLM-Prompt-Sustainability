import unittest
from mbpp_137_code import zero_count

class TestZeroCount(unittest.TestCase):
    def test_typical_case(self):
        self.assertAlmostEqual(zero_count([1, 2, 3, 0, 5, 0]), 0.4)

    def test_edge_case_empty(self):
        self.assertAlmostEqual(zero_count([]), 0.0)

    def test_edge_case_all_zero(self):
        self.assertAlmostEqual(zero_count([0, 0, 0]), 1.0)

    def test_edge_case_single_zero(self):
        self.assertAlmostEqual(zero_count([1, 0, 1]), 0.33333333333333337)
