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

    def test_edge_case_with_empty_array(self):
        arr = []
        n = len(arr)
        expected_output = []
        self.assertEqual(re_arrange(arr, n), expected_output)

    def test_typical_case_with_negative_numbers(self):
        arr = [-1, -2, -3, -4, -5]
        n = len(arr)
        expected_output = [-1, -2, -3, -4, -5]
        self.assertEqual(re_arrange(arr, n), expected_output)

    def test_typical_case_with_mixed_numbers(self):
        arr = [1, -2, 3, -4, 5]
        n = len(arr)
        expected_output = [1, -2, 3, -4, 5]
        self.assertEqual(re_arrange(arr, n), expected_output)

    def test_error_case_with_non_integer_elements(self):
        arr = [1, -2, 'a', -4, 5]
        n = len(arr)
        with self.assertRaises(TypeError):
            re_arrange(arr, n)
