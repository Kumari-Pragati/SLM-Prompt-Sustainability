import unittest
from mbpp_286_code import max_sub_array_sum_repeated

class TestMaxSubArraySumRepeated(unittest.TestCase):
    def test_simple_valid_input(self):
        self.assertEqual(max_sub_array_sum_repeated([1, 2, 3, 4, 5], 5, 1), 9)

    def test_edge_case_empty_input(self):
        self.assertEqual(max_sub_array_sum_repeated([], 0, 1), -2147483648)

    def test_edge_case_single_element_input(self):
        self.assertEqual(max_sub_array_sum_repeated([1], 1, 1), 1)

    def test_edge_case_zero_input(self):
        self.assertEqual(max_sub_array_sum_repeated([0, 0, 0, 0, 0], 5, 1), 0)

    def test_edge_case_negative_input(self):
        self.assertEqual(max_sub_array_sum_repeated([-1, -2, -3, -4, -5], 5, 1), -1)

    def test_edge_case_max_input(self):
        self.assertEqual(max_sub_array_sum_repeated([2147483647, 2147483647, 2147483647, 2147483647, 2147483647], 5, 1), 2147483647)

    def test_edge_case_min_input(self):
        self.assertEqual(max_sub_array_sum_repeated([-2147483648, -2147483648, -2147483648, -2147483648, -2147483648], 5, 1), -2147483648)

    def test_edge_case_k_greater_than_n(self):
        self.assertEqual(max_sub_array_sum_repeated([1, 2, 3, 4, 5], 5, 10), 9)

    def test_edge_case_k_equal_to_n(self):
        self.assertEqual(max_sub_array_sum_repeated([1, 2, 3, 4, 5], 5, 5), 9)

    def test_edge_case_k_less_than_n(self):
        self.assertEqual(max_sub_array_sum_repeated([1, 2, 3, 4, 5], 5, 1), 9)
