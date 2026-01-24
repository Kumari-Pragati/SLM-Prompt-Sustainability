import unittest
from mbpp_229_code import re_arrange_array

class TestReArrangeArray(unittest.TestCase):
    def test_positive_numbers(self):
        arr = [1, 2, -3, 4, -5, 6]
        expected = [1, 2, -3, 4, 6, -5]
        self.assertEqual(re_arrange_array(arr, len(arr)), expected)

    def test_empty_array(self):
        arr = []
        self.assertEqual(re_arrange_array(arr, 0), arr)

    def test_single_negative_number(self):
        arr = [-1]
        expected = [-1]
        self.assertEqual(re_arrange_array(arr, len(arr)), expected)

    def test_negative_numbers_only(self):
        arr = [-1, -2, -3]
        expected = [-1, -2, -3]
        self.assertEqual(re_arrange_array(arr, len(arr)), expected)

    def test_all_zero(self):
        arr = [0, 0, 0]
        expected = [0, 0, 0]
        self.assertEqual(re_arrange_array(arr, len(arr)), expected)

    def test_negative_and_positive_numbers(self):
        arr = [1, -2, 3, -4]
        expected = [1, -2, 3, -4]
        self.assertEqual(re_arrange_array(arr, len(arr)), expected)

    def test_invalid_input_length(self):
        with self.assertRaises(ValueError):
            re_arrange_array(arr, len(arr) - 1)
