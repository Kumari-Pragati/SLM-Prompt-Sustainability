import unittest
from mbpp_229_code import re_arrange_array

class TestReArrangeArray(unittest.TestCase):

    def test_normal_case(self):
        self.assertListEqual(re_arrange_array([-1, 2, -3, 4, -5, 6], 6), [-1, 2, -3, 4, -5, 6])
        self.assertListEqual(re_arrange_array([-1, -2, -3, -4, -5], 5), [-1, -2, -3, -4, -5])
        self.assertListEqual(re_arrange_array([-1, 0, -2, 0, -3, 0], 6), [-1, 0, -2, 0, -3, 0])

    def test_edge_cases(self):
        self.assertListEqual(re_arrange_array([-1], 1), [-1])
        self.assertListEqual(re_arrange_array([0], 1), [0])
        self.assertListEqual(re_arrange_array([-1, 0], 2), [-1, 0])
        self.assertListEqual(re_arrange_array([-1, 0, -1], 3), [-1, 0, -1])

    def test_boundary_cases(self):
        self.assertListEqual(re_arrange_array([-1, 0], 0), [0])
        self.assertListEqual(re_arrange_array([-1, 0], -1), [0])

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            re_arrange_array('invalid', 1)
        with self.assertRaises(TypeError):
            re_arrange_array([1], 'invalid')
