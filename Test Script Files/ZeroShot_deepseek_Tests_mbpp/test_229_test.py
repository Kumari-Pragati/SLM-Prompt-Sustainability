import unittest
from mbpp_229_code import re_arrange_array

class TestRearrangeArray(unittest.TestCase):

    def test_positive_and_negative_numbers(self):
        arr = [1, -2, 3, -4, 5, -6]
        n = len(arr)
        expected_output = [-2, -4, -6, 1, 3, 5]
        self.assertEqual(re_arrange_array(arr, n), expected_output)

    def test_all_positive_numbers(self):
        arr = [1, 2, 3, 4, 5]
        n = len(arr)
        expected_output = [1, 2, 3, 4, 5]
        self.assertEqual(re_arrange_array(arr, n), expected_output)

    def test_all_negative_numbers(self):
        arr = [-1, -2, -3, -4, -5]
        n = len(arr)
        expected_output = [-1, -2, -3, -4, -5]
        self.assertEqual(re_arrange_array(arr, n), expected_output)

    def test_mixed_positive_and_negative_numbers(self):
        arr = [-1, 2, -3, 4, -5]
        n = len(arr)
        expected_output = [-1, -3, -5, 2, 4]
        self.assertEqual(re_arrange_array(arr, n), expected_output)

    def test_empty_array(self):
        arr = []
        n = len(arr)
        expected_output = []
        self.assertEqual(re_arrange_array(arr, n), expected_output)
