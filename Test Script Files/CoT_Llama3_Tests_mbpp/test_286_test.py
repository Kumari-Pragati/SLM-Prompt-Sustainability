import unittest
from mbpp_286_code import max_sub_array_sum_repeated

class TestMaxSubArraySumRepeated(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(max_sub_array_sum_repeated([1, 2, 3, 4, 5], 5, 1), 9)

    def test_edge_case_zero_sum(self):
        self.assertEqual(max_sub_array_sum_repeated([0, 0, 0, 0, 0], 5, 1), 0)

    def test_edge_case_single_element(self):
        self.assertEqual(max_sub_array_sum_repeated([1], 1, 1), 1)

    def test_edge_case_negative_numbers(self):
        self.assertEqual(max_sub_array_sum_repeated([-1, -2, -3, -4, -5], 5, 1), -1)

    def test_edge_case_k_greater_than_n(self):
        self.assertEqual(max_sub_array_sum_repeated([1, 2, 3, 4, 5], 5, 10), 9)

    def test_edge_case_k_equal_to_n(self):
        self.assertEqual(max_sub_array_sum_repeated([1, 2, 3, 4, 5], 5, 5), 9)

    def test_edge_case_k_zero(self):
        self.assertEqual(max_sub_array_sum_repeated([1, 2, 3, 4, 5], 5, 0), 0)
