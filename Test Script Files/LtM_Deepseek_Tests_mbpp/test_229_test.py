import unittest
from mbpp_229_code import re_arrange_array

class TestRearrangeArray(unittest.TestCase):

    def test_simple_positive_numbers(self):
        self.assertEqual(re_arrange_array([1, 2, 3, 4, 5], 5), [1, 2, 3, 4, 5])

    def test_simple_negative_numbers(self):
        self.assertEqual(re_arrange_array([-1, -2, -3, -4, -5], 5), [-1, -2, -3, -4, -5])

    def test_mixed_positive_negative_numbers(self):
        self.assertEqual(re_arrange_array([-1, 2, -3, 4, -5], 5), [-1, 2, -3, 4, -5])

    def test_empty_array(self):
        self.assertEqual(re_arrange_array([], 0), [])

    def test_single_element_array(self):
        self.assertEqual(re_arrange_array([1], 1), [1])

    def test_all_positive_array(self):
        self.assertEqual(re_arrange_array([1, 2, 3, 4, 5], 5), [1, 2, 3, 4, 5])

    def test_all_negative_array(self):
        self.assertEqual(re_arrange_array([-1, -2, -3, -4, -5], 5), [-1, -2, -3, -4, -5])

    def test_mixed_positive_negative_array(self):
        self.assertEqual(re_arrange_array([-1, 2, -3, 4, -5], 5), [-1, 2, -3, 4, -5])
