import unittest
from mbpp_734_code import sum_Of_Subarray_Prod

class TestSumOfSubarrayProd(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(sum_Of_Subarray_Prod([1, 2, 3, 4], 4), 10)
        self.assertEqual(sum_Of_Subarray_Prod([0, 0, 0, 0], 4), 0)
        self.assertEqual(sum_Of_Subarray_Prod([1, 2, 3], 3), 9)
        self.assertEqual(sum_Of_Subarray_Prod([1], 1), 1)

    def test_edge_cases(self):
        self.assertEqual(sum_Of_Subarray_Prod([1, 2, 3, 4], 1), 0)
        self.assertEqual(sum_Of_Subarray_Prod([1, 2, 3, 4], 0), 0)
        self.assertEqual(sum_Of_Subarray_Prod([], 0), 0)
        self.assertEqual(sum_Of_Subarray_Prod([1, 2, 3, 4], 5), 20)

    def test_complex(self):
        self.assertEqual(sum_Of_Subarray_Prod([1, 0, 2, 0, 3, 0, 4], 7), 24)
        self.assertEqual(sum_Of_Subarray_Prod([-1, -2, -3, -4], 4), -24)
        self.assertEqual(sum_Of_Subarray_Prod([100, 200, 300, 400], 4), 1479)
