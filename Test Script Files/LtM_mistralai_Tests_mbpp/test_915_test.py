import unittest
from mbpp_915_code import rearrange_numbs

class TestRearrangeNumbs(unittest.TestCase):
    def test_simple_positive(self):
        self.assertListEqual(rearrange_numbs([1, 2, 3]), [1, 2, 3])

    def test_simple_negative(self):
        self.assertListEqual(rearrange_numbs([-1, -2, -3]), [-3, -2, -1])

    def test_simple_mixed(self):
        self.assertListEqual(rearrange_numbs([1, -2, 3]), [1, -2, 3])

    def test_edge_zero(self):
        self.assertListEqual(rearrange_numbs([0, 1, 2]), [0, 1, 2])

    def test_edge_negative_zero(self):
        self.assertListEqual(rearrange_numbs([-0, -1, -2]), [-2, -1, -0])

    def test_edge_positive_zero(self):
        self.assertListEqual(rearrange_numbs([1, 0, 2]), [1, 0, 2])

    def test_edge_min(self):
        self.assertListEqual(rearrange_numbs([-1 * 1e100, -2, -3]), [-2, -3, -1 * 1e100])

    def test_edge_max(self):
        self.assertListEqual(rearrange_numbs([1 * 1e100, 2, 3]), [2, 3, 1 * 1e100])

    def test_complex_mixed(self):
        self.assertListEqual(rearrange_numbs([0, 1, -2, 3, 0, -0.5]), [0, 0, -0.5, -2, 1, -0])
