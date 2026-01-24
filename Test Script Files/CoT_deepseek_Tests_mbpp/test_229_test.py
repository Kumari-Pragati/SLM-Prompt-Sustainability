import unittest
from mbpp_229_code import re_arrange_array

class TestRearrangeArray(unittest.TestCase):

    def test_typical_case(self):
        arr = [10, -1, 20, -30, 40, -50]
        n = len(arr)
        expected_output = [-1, 10, -30, 20, -50, 40]
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

    def test_mixed_positive_negative(self):
        arr = [-10, 20, -30, 40, -50]
        n = len(arr)
        expected_output = [-10, 20, -30, 40, -50]
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
