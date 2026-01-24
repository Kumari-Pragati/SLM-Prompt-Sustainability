import unittest
from mbpp_323_code import re_arrange

class TestRearrangeFunction(unittest.TestCase):

    def test_typical_case(self):
        arr = [1, -2, 3, -4, 5]
        n = len(arr)
        expected_output = [1, -2, 3, -4, 5]
        self.assertEqual(re_arrange(arr, n), expected_output)

    def test_edge_case_with_single_element(self):
        arr = [1]
        n = len(arr)
        expected_output = [1]
        self.assertEqual(re_arrange(arr, n), expected_output)

    def test_edge_case_with_two_elements(self):
        arr = [1, -1]
        n = len(arr)
        expected_output = [1, -1]
        self.assertEqual(re_arrange(arr, n), expected_output)

    def test_boundary_case_with_negative_numbers(self):
        arr = [-1, -2, -3, -4, -5]
        n = len(arr)
        expected_output = [-1, -2, -3, -4, -5]
        self.assertEqual(re_arrange(arr, n), expected_output)

    def test_boundary_case_with_positive_numbers(self):
        arr = [1, 2, 3, 4, 5]
        n = len(arr)
        expected_output = [1, 2, 3, 4, 5]
        self.assertEqual(re_arrange(arr, n), expected_output)

    def test_invalid_input_with_mixed_numbers(self):
        arr = [1, -2, 3, -4, 5]
        n = 4
        with self.assertRaises(IndexError):
            re_arrange(arr, n)

    def test_invalid_input_with_empty_array(self):
        arr = []
        n = 0
        expected_output = []
        self.assertEqual(re_arrange(arr, n), expected_output)
