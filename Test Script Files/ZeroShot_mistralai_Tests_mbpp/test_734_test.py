import unittest
from mbpp_734_code import sum_Of_Subarray_Prod

class TestSumOfSubarrayProd(unittest.TestCase):

    def test_empty_array(self):
        self.assertEqual(sum_Of_Subarray_Prod([], 0), 0)

    def test_single_element_array(self):
        self.assertEqual(sum_Of_Subarray_Prod([1], 1), 1)

    def test_simple_array(self):
        self.assertEqual(sum_Of_Subarray_Prod([1, 2, 3, 4], 4), 31)

    def test_negative_numbers(self):
        self.assertEqual(sum_Of_Subarray_Prod([-1, -2, -3, -4], 4), -31)

    def test_zero_element(self):
        self.assertEqual(sum_Of_Subarray_Prod([0], 1), 0)

    def test_large_array(self):
        self.assertEqual(sum_Of_Subarray_Prod([1, 2, 3, 4, 5, 6, 7, 8, 9], 9), 389)
