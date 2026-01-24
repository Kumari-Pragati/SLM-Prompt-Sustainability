import unittest
from mbpp_229_code import re_arrange_array

class TestRearrangeArray(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(re_arrange_array([-1, 2, -3, 4, -5], 5), [-1, -3, -5, 2, 4])

    def test_empty_array(self):
        self.assertEqual(re_arrange_array([], 0), [])

    def test_all_positive(self):
        self.assertEqual(re_arrange_array([1, 2, 3, 4, 5], 5), [1, 2, 3, 4, 5])

    def test_all_negative(self):
        self.assertEqual(re_arrange_array([-1, -2, -3, -4, -5], 5), [-1, -2, -3, -4, -5])

    def test_mixed_positive_negative(self):
        self.assertEqual(re_arrange_array([-1, 2, -3, 4, -5], 5), [-1, -3, -5, 2, 4])

    def test_single_element(self):
        self.assertEqual(re_arrange_array([-1], 1), [-1])

    def test_single_positive_element(self):
        self.assertEqual(re_arrange_array([1], 1), [1])

    def test_large_array(self):
        self.assertEqual(re_arrange_array(list(range(-1000, 1000, 2)), 2000), list(range(-1000, 1000, 2)))
