import unittest
from mbpp_229_code import re_arrange_array

class TestReArrangeArray(unittest.TestCase):

    def test_simple(self):
        self.assertListEqual(re_arrange_array([-1, 2, -3, 4], 4), [-1, 4, -3, 2])
        self.assertListEqual(re_arrange_array([-5, -4, -3, -2, -1, 0, 1, 2, 3, 4], 10), [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4])

    def test_edge_cases(self):
        self.assertListEqual(re_arrange_array([-1], 1), [-1])
        self.assertListEqual(re_arrange_array([0, -1], 2), [0, -1])
        self.assertListEqual(re_arrange_array([-1, 0], 2), [-1, 0])
        self.assertListEqual(re_arrange_array([-1, -2], 2), [-2, -1])
        self.assertListEqual(re_arrange_array([-1, -2, 0], 3), [-1, 0, -2])

    def test_boundary_conditions(self):
        self.assertListEqual(re_arrange_array([-1], 0), [])
        self.assertListEqual(re_arrange_array([], 0), [])
        self.assertListEqual(re_arrange_array([0], 0), [])
        self.assertListEqual(re_arrange_array([1], 0), [])
        self.assertListEqual(re_arrange_array([-1, 0], 1), [-1])
        self.assertListEqual(re_arrange_array([0, -1], 1), [-1])
