import unittest
from mbpp_734_code import sum_Of_Subarray_Prod

class TestSumOfSubarrayProd(unittest.TestCase):

    def test_typical_case(self):
        arr = [1, 2, 3, 4]
        n = len(arr)
        self.assertEqual(sum_Of_Subarray_Prod(arr, n), 50)

    def test_edge_case_single_element(self):
        arr = [5]
        n = len(arr)
        self.assertEqual(sum_Of_Subarray_Prod(arr, n), 5)

    def test_edge_case_empty_array(self):
        arr = []
        n = len(arr)
        self.assertEqual(sum_Of_Subarray_Prod(arr, n), 0)

    def test_error_case_negative_elements(self):
        arr = [-1, -2, -3, -4]
        n = len(arr)
        self.assertEqual(sum_Of_Subarray_Prod(arr, n), -50)

    def test_error_case_zero_elements(self):
        arr = [0, 0, 0, 0]
        n = len(arr)
        self.assertEqual(sum_Of_Subarray_Prod(arr, n), 0)
