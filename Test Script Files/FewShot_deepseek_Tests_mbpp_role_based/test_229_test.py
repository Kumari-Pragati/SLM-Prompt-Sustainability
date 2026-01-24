import unittest
from mbpp_229_code import re_arrange_array

class TestRearrangeArray(unittest.TestCase):
    def test_typical_case(self):
        arr = [10, -1, 20, -30, 40, -50]
        n = len(arr)
        expected_output = [-1, -30, -50, 10, 20, 40]
        self.assertEqual(re_arrange_array(arr, n), expected_output)

    def test_all_positive(self):
        arr = [10, 20, 30, 40, 50]
        n = len(arr)
        expected_output = [10, 20, 30, 40, 50]
        self.assertEqual(re_arrange_array(arr, n), expected_output)

    def test_all_negative(self):
        arr = [-10, -20, -30, -40, -50]
        n = len(arr)
        expected_output = [-10, -20, -30, -40, -50]
        self.assertEqual(re_arrange_array(arr, n), expected_output)

    def test_empty_array(self):
        arr = []
        n = 0
        expected_output = []
        self.assertEqual(re_arrange_array(arr, n), expected_output)

    def test_single_element(self):
        arr = [10]
        n = 1
        expected_output = [10]
        self.assertEqual(re_arrange_array(arr, n), expected_output)

    def test_large_array(self):
        arr = [i for i in range(-1000, 1000, 2)]
        n = len(arr)
        expected_output = [-1, -3, -5, ..., 995, 997]  # Note: This is a placeholder for the actual expected output.
        self.assertEqual(re_arrange_array(arr, n), expected_output)
