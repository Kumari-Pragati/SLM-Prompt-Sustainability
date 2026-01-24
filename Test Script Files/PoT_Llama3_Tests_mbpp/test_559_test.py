import unittest
from mbpp_559_code import max_sub_array_sum

class TestMaxSubArraySum(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(max_sub_array_sum([-2,1,-3,4,-1,2,1,-5,4], 9), 6)

    def test_edge_case_all_negative(self):
        self.assertEqual(max_sub_array_sum([-1,-2,-3,-4,-5], 5), -1)

    def test_edge_case_all_positive(self):
        self.assertEqual(max_sub_array_sum([1,2,3,4,5], 5), 15)

    def test_edge_case_single_element(self):
        self.assertEqual(max_sub_array_sum([1], 1), 1)

    def test_edge_case_empty_array(self):
        self.assertEqual(max_sub_array_sum([], 0), 0)

    def test_edge_case_single_element_zero(self):
        self.assertEqual(max_sub_array_sum([0], 1), 0)

    def test_edge_case_single_element_negative(self):
        self.assertEqual(max_sub_array_sum([-1], 1), -1)

    def test_edge_case_subarray_with_zero(self):
        self.assertEqual(max_sub_array_sum([1,2,0,3,4], 5), 7)

    def test_edge_case_subarray_with_negative(self):
        self.assertEqual(max_sub_array_sum([-1,-2,-3,-4,-5], 5), -1)
