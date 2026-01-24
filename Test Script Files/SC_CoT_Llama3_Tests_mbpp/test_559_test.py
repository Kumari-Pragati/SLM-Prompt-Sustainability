import unittest
from mbpp_559_code import max_sub_array_sum

class TestMaxSubArraySum(unittest.TestCase):
    def test_typical_input(self):
        self.assertEqual(max_sub_array_sum([-2,1,-3,4,-1,2,1,-5,4], 7), 6)

    def test_edge_case_negative(self):
        self.assertEqual(max_sub_array_sum([-2,-3,-4], 3), -1)

    def test_edge_case_positive(self):
        self.assertEqual(max_sub_array_sum([1,2,3,4], 4), 10)

    def test_edge_case_single_element(self):
        self.assertEqual(max_sub_array_sum([1], 1), 1)

    def test_edge_case_empty(self):
        self.assertEqual(max_sub_array_sum([], 0), 0)

    def test_edge_case_single_element_zero(self):
        self.assertEqual(max_sub_array_sum([0], 1), 0)

    def test_edge_case_single_element_negative(self):
        self.assertEqual(max_sub_array_sum([-1], 1), -1)

    def test_edge_case_subarray_sum_zero(self):
        self.assertEqual(max_sub_array_sum([-1,0,1], 3), 0)

    def test_edge_case_subarray_sum_negative(self):
        self.assertEqual(max_sub_array_sum([-2,-1,0,1], 4), 1)

    def test_edge_case_subarray_sum_positive(self):
        self.assertEqual(max_sub_array_sum([1,2,3,4], 4), 10)

    def test_edge_case_subarray_sum_zero(self):
        self.assertEqual(max_sub_array_sum([1,2,3,4], 4), 10)
