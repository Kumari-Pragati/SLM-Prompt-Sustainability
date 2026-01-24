import unittest
from mbpp_734_code import sum_Of_Subarray_Prod

class TestSumOfSubarrayProd(unittest.TestCase):

    def test_empty_array(self):
        self.assertEqual(sum_Of_Subarray_Prod([], 0), 0)

    def test_single_element_array(self):
        for num in range(1, 101):
            self.assertEqual(sum_Of_Subarray_Prod([num], 1), num)

    def test_positive_array(self):
        test_arrays = [
            [1, 2, 3, 4, 5],
            [10, 20, 30, 40, 50],
            [-1, -2, -3, -4, -5]
        ]
        for arr in test_arrays:
            for n in range(1, len(arr) + 1):
                self.assertEqual(sum_Of_Subarray_Prod(arr, n), expected_sum)
                expected_sum = sum(arr[:n])

    def test_negative_n(self):
        self.assertRaises(IndexError, sum_Of_Subarray_Prod, [1, 2, 3], -1)

    def test_zero_n(self):
        self.assertEqual(sum_Of_Subarray_Prod([1, 2, 3], 0), 0)
