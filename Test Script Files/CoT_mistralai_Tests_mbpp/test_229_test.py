import unittest
from mbpp_229_code import re_arrange_array

class TestReArrangeArray(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertListEqual(re_arrange_array([1, 2, 3, -1, 5, -2], 6), [1, 2, 3, 5, 1, -2])
        self.assertListEqual(re_arrange_array([4, 0, 3, -1, 2], 5), [4, 0, 3, 2, -1])
        self.assertListEqual(re_arrange_array([], 0), [])

    def test_negative_numbers_only(self):
        self.assertListEqual(re_arrange_array([-1, -2, -3], 3), [-1, -2, -3])

    def test_single_negative_number(self):
        self.assertListEqual(re_arrange_array([1, -2, 3], 3), [1, 3, -2])

    def test_boundary_conditions(self):
        self.assertListEqual(re_arrange_array([-1], 1), [-1])
        self.assertListEqual(re_arrange_array([-1, -2], 2), [-2, -1])

    def test_invalid_input_length(self):
        with self.assertRaises(IndexError):
            re_arrange_array([-1], 0)

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            re_arrange_array('abc', 1)
