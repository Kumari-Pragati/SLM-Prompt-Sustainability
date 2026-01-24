import unittest
from mbpp_229_code import re_arrange_array

class TestRearrangeArray(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(re_arrange_array([-1, 2, -3, 4, 5, -6], 6), [-1, -3, -6, 2, 4, 5])

    def test_edge_case_single_negative(self):
        self.assertEqual(re_arrange_array([-1], 1), [-1])

    def test_edge_case_single_positive(self):
        self.assertEqual(re_arrange_array([1], 1), [1])

    def test_edge_case_all_negative(self):
        self.assertEqual(re_arrange_array([-1, -2, -3], 3), [-1, -2, -3])

    def test_edge_case_all_positive(self):
        self.assertEqual(re_arrange_array([1, 2, 3], 3), [1, 2, 3])

    def test_edge_case_empty_array(self):
        self.assertEqual(re_arrange_array([], 0), [])

    def test_corner_case_mixed_numbers(self):
        self.assertEqual(re_arrange_array([-1, 0, 1], 3), [-1, 0, 1])

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            re_arrange_array("not an array", 0)

    def test_invalid_input_negative_length(self):
        with self.assertRaises(ValueError):
            re_arrange_array([1, 2, 3], -1)
