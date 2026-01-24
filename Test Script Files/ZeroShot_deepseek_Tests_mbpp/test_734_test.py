import unittest
from mbpp_734_code import sum_Of_Subarray_Prod

class TestSumOfSubarrayProd(unittest.TestCase):

    def test_sum_Of_Subarray_Prod(self):
        self.assertEqual(sum_Of_Subarray_Prod([1, 2, 3, 4], 4), 50)
        self.assertEqual(sum_Of_Subarray_Prod([1, 0, 1], 3), 3)
        self.assertEqual(sum_Of_Subarray_Prod([10, 20, 30, 40], 4), 1000)
        self.assertEqual(sum_Of_Subarray_Prod([1, 2, 3], 3), 10)
