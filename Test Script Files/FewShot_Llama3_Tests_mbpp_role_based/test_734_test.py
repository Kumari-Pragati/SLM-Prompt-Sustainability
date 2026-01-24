import unittest
from mbpp_734_code import sum_Of_Subarray_Prod

class TestSumOfSubarrayProd(unittest.TestCase):
    def test_typical_use_case(self):
        arr = [1, 2, 3, 4, 5]
        n = len(arr)
        self.assertEqual(sum_Of_Subarray_Prod(arr, n), 30)

    def test_edge_case_empty_array(self):
        arr = []
        n = len(arr)
        self.assertEqual(sum_Of_Subarray_Prod(arr, n), 0)

    def test_edge_case_single_element_array(self):
        arr = [5]
        n = len(arr)
        self.assertEqual(sum_Of_Subarray_Prod(arr, n), 5)

    def test_edge_case_zero_length_array(self):
        arr = [1, 2, 3, 0, 4, 5]
        n = len(arr)
        self.assertEqual(sum_Of_Subarray_Prod(arr, n), 15)

    def test_edge_case_negative_numbers(self):
        arr = [-1, -2, -3, -4, -5]
        n = len(arr)
        self.assertEqual(sum_Of_Subarray_Prod(arr, n), -30)

    def test_edge_case_mixed_positive_and_negative_numbers(self):
        arr = [1, -2, 3, -4, 5]
        n = len(arr)
        self.assertEqual(sum_Of_Subarray_Prod(arr, n), 15)
