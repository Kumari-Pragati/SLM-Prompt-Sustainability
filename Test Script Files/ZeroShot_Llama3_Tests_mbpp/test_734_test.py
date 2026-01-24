import unittest
from mbpp_734_code import sum_Of_Subarray_Prod

class TestSumOfSubarrayProd(unittest.TestCase):

    def test_sum_Of_Subarray_Prod(self):
        self.assertEqual(sum_Of_Subarray_Prod([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10), 3025)
        self.assertEqual(sum_Of_Subarray_Prod([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10], 10), -385)
        self.assertEqual(sum_Of_Subarray_Prod([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], 10), 3025)
        self.assertEqual(sum_Of_Subarray_Prod([1, 2, 3, 4, 5, 6, 7, 8, 9, -1], 10), 3024)
        self.assertEqual(sum_Of_Subarray_Prod([-1, -2, -3, -4, -5, -6, -7, -8, -9, 0], 10), -384)
