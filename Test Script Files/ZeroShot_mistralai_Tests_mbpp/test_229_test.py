import unittest
from mbpp_229_code import re_arrange_array

class TestReArrangeArray(unittest.TestCase):

    def test_empty_array(self):
        self.assertEqual(re_arrange_array([], 0), [])

    def test_single_negative_element(self):
        self.assertEqual(re_arrange_Array([-1], 1), [0, -1])

    def test_single_positive_element(self):
        self.assertEqual(re_arrange_Array([1], 1), [1])

    def test_mixed_elements(self):
        self.assertEqual(re_arrange_Array([-1, 1, -2, 3, -4, 5], 6), [5, 3, -4, -2, -1, 1])

    def test_all_negative_elements(self):
        self.assertEqual(re_arrange_Array([-1, -2, -3], 3), [0, -1, -2, -3])

    def test_all_positive_elements(self):
        self.assertEqual(re_arrange_Array([1, 2, 3], 3), [1, 2, 3])
