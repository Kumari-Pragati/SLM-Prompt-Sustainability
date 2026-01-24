import unittest
from mbpp_734_code import sum_Of_Subarray_Prod

class TestSumOfSubarrayProd(unittest.TestCase):

    def test_typical_input(self):
        self.assertEqual(sum_Of_Subarray_Prod([1, 2, 3, 4, 5], 5), 15)

    def test_edge_case_zero_length(self):
        self.assertEqual(sum_Of_Subarray_Prod([], 0), 0)

    def test_edge_case_single_element(self):
        self.assertEqual(sum_Of_Subarray_Prod([1], 1), 1)

    def test_edge_case_single_element_zero(self):
        self.assertEqual(sum_Of_Subarray_Prod([0], 1), 0)

    def test_edge_case_single_element_negative(self):
        self.assertEqual(sum_Of_Subarray_Prod([-1], 1), -1)

    def test_edge_case_negative_length(self):
        with self.assertRaises(IndexError):
            sum_Of_Subarray_Prod([1, 2, 3], -1)

    def test_edge_case_empty_list(self):
        with self.assertRaises(IndexError):
            sum_Of_Subarray_Prod([], -1)

    def test_edge_case_negative_elements(self):
        self.assertEqual(sum_Of_Subarray_Prod([-1, -2, -3, -4, -5], 5), -15)

    def test_edge_case_mixed_elements(self):
        self.assertEqual(sum_Of_Subarray_Prod([1, 2, -3, 4, -5], 5), 0)

    def test_edge_case_all_positive(self):
        self.assertEqual(sum_Of_Subarray_Prod([1, 2, 3, 4, 5], 5), 15)

    def test_edge_case_all_negative(self):
        self.assertEqual(sum_Of_Subarray_Prod([-1, -2, -3, -4, -5], 5), -15)
