import unittest
from mbpp_229_code import re_arrange_array

class TestReArrangeArray(unittest.TestCase):

    def test_empty_array(self):
        self.assertListEqual(re_arrange_array([], 0), [])

    def test_single_negative_element(self):
        self.assertListEqual(re_arrange_array([-1], 1), [0, -1])

    def test_single_positive_element(self):
        self.assertListEqual(re_arrange_array([1], 1), [1])

    def test_multiple_negative_elements(self):
        self.assertListEqual(re_arrange_array([-1, -2, -3], 3), [0, -3, -2, -1])

    def test_multiple_positive_elements(self):
        self.assertListEqual(re_arrange_array([1, 2, 3], 3), [1, 2, 3])

    def test_mixed_elements(self):
        self.assertListEqual(re_arrange_array([-1, 0, 1, -2], 4), [0, -2, -1, 1])

    def test_negative_index(self):
        with self.assertRaises(IndexError):
            re_arrange_array([-1], -1)

    def test_zero_length_array(self):
        with self.assertRaises(ValueError):
            re_arrange_array([], n=0)

    def test_negative_n(self):
        with self.assertRaises(ValueError):
            re_arrange_array([-1], n=-1)
