import unittest
from mbpp_245_code import max_sum

class TestMaxSum(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(max_sum([1, 2, 3, 4], 4), 10)

    def test_edge_case_single_element(self):
        self.assertEqual(max_sum([5], 1), 5)

    def test_edge_case_negative_elements(self):
        self.assertEqual(max_sum([-1, -2, -3, -4], 4), -1)

    def test_edge_case_same_elements(self):
        self.assertEqual(max_sum([1, 1, 1, 1], 4), 4)

    def test_edge_case_empty_array(self):
        self.assertEqual(max_sum([], 0), float("-inf"))

    def test_invalid_input_negative_length(self):
        with self.assertRaises(Exception):
            max_sum([1, 2, 3, 4], -1)

    def test_invalid_input_non_integer_elements(self):
        with self.assertRaises(Exception):
            max_sum([1, 2, '3', 4], 4)
