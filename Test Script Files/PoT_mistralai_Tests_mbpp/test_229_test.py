import unittest
from mbpp_229_code import re_arrange_array

class TestReArrangeArray(unittest.TestCase):

    def test_typical_case(self):
        self.assertListEqual(re_arrange_array([-1, 2, -3, 4, -5, 6], 6), [-1, 2, -3, 4, 6, -5])
        self.assertListEqual(re_arrange_array([-1, -2, -3, -4, -5], 5), [-1, -2, -3, -4, -5])
        self.assertListEqual(re_arrange_array([-1, -2, -3, -4, -5, -6], 6), [-1, -2, -3, -4, -5, -6])

    def test_edge_case_empty_list(self):
        self.assertListEqual(re_arrange_array([], 0), [])

    def test_edge_case_single_negative_number(self):
        self.assertListEqual(re_arrange_array([-1], 1), [-1])

    def test_edge_case_single_positive_number(self):
        self.assertListEqual(re_arrange_array([1], 1), [1])

    def test_edge_case_all_positive_numbers(self):
        self.assertListEqual(re_arrange_array([1, 2, 3, 4, 5], 5), [1, 2, 3, 4, 5])

    def test_edge_case_all_negative_numbers(self):
        self.assertListEqual(re_arrange_array([-1, -2, -3, -4, -5], 5), [-1, -2, -3, -4, -5])

    def test_corner_case_negative_numbers_in_middle(self):
        self.assertListEqual(re_arrange_array([1, -2, 3, -4, 5], 5), [1, -2, 3, 5, -4])

    def test_corner_case_negative_numbers_at_beginning(self):
        self.assertListEqual(re_arrange_array([-1, 2, 3, 4, 5], 5), [-1, 2, 3, 4, 5])

    def test_corner_case_negative_numbers_at_end(self):
        self.assertListEqual(re_arrange_array([1, 2, 3, -4, -5], 5), [1, 2, 3, -4, -5])
