import unittest
from mbpp_915_code import rearrange_numbs

class TestRearrangeNumbs(unittest.TestCase):

    def test_typical_case(self):
        self.assertListEqual(rearrange_numbs([1, -2, 3, 0, 4, -5]), [0, 1, -2, -5, 3, 4])

    def test_edge_case_positive(self):
        self.assertListEqual(rearrange_numbs([1000000000]), [0, 1000000000])

    def test_edge_case_negative(self):
        self.assertListEqual(rearrange_numbs([-1000000000]), [-1000000000, 0])

    def test_boundary_case_zero(self):
        self.assertListEqual(rearrange_numbs([0]), [0])

    def test_boundary_case_one(self):
        self.assertListEqual(rearrange_numbs([1]), [1])

    def test_corner_case_negative_zero(self):
        self.assertListEqual(rearrange_numbs([-0]), [-0])
