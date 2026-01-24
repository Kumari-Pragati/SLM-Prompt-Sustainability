import unittest
from mbpp_734_code import sum_Of_Subarray_Prod

class TestSumOfSubarrayProd(unittest.TestCase):
    def test_typical_use_case(self):
        arr = [1, 2, 3, 4]
        n = len(arr)
        self.assertEqual(sum_Of_Subarray_Prod(arr, n), 50)

    def test_edge_condition(self):
        arr = [0]
        n = len(arr)
        self.assertEqual(sum_Of_Subarray_Prod(arr, n), 0)

    def test_boundary_condition(self):
        arr = [1, 2, 3, 4, 5]
        n = len(arr)
        self.assertEqual(sum_Of_Subarray_Prod(arr, n), 40)

    def test_invalid_input(self):
        arr = [1, 2, 3, 4]
        n = -1
        with self.assertRaises(Exception):
            sum_Of_Subarray_Prod(arr, n)
