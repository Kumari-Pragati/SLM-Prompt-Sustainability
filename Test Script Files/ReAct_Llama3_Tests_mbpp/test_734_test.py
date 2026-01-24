import unittest
from mbpp_734_code import sum_Of_Subarray_Prod

class TestSumOfSubarrayProd(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(sum_Of_Subarray_Prod([1, 2, 3, 4, 5], 5), 15)

    def test_edge_case_empty_array(self):
        self.assertEqual(sum_Of_Subarray_Prod([], 0), 0)

    def test_edge_case_single_element_array(self):
        self.assertEqual(sum_Of_Subarray_Prod([1], 1), 1)

    def test_edge_case_zero_length_array(self):
        self.assertEqual(sum_Of_Subarray_Prod([1, 2, 3], 0), 0)

    def test_edge_case_negative_numbers(self):
        self.assertEqual(sum_Of_Subarray_Prod([-1, -2, -3, -4, -5], 5), -15)

    def test_edge_case_positive_numbers(self):
        self.assertEqual(sum_Of_Subarray_Prod([1, 2, 3, 4, 5], 5), 15)

    def test_edge_case_mixed_numbers(self):
        self.assertEqual(sum_Of_Subarray_Prod([-1, 2, -3, 4, -5], 5), -5)
