import unittest
from mbpp_915_code import rearrange_numbs

class TestRearrangeNumbs(unittest.TestCase):
    def test_normal_input(self):
        self.assertListEqual(rearrange_numbs([1, 2, 0, 4, 0, 3]), [0, 0, 1, 2, 3, 4])
        self.assertListEqual(rearrange_numbs([-1, 0, 1, 2, 3]), [-1, 0, 1, 2, 3])

    def test_edge_and_boundary_conditions(self):
        self.assertListEqual(rearrange_numbs([0]), [0])
        self.assertListEqual(rearrange_numbs([0, 0]), [0, 0])
        self.assertListEqual(rearrange_numbs([-1, -2, -3]), [-3, -2, -1])
        self.assertListEqual(rearrange_numbs([1e100, -1e100]), [1e100, -1e100])

    def test_negative_numbers(self):
        self.assertListEqual(rearrange_numbs([-1, -2, -3]), [-3, -2, -1])
        self.assertListEqual(rearrange_numbs([-1, 0, -2]), [-2, 0, -1])

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            rearrange_numbs(1.5)
        with self.assertRaises(TypeError):
            rearrange_numbs([])
