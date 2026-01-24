import unittest
from mbpp_734_code import sum_Of_Subarray_Prod

class TestSumOfSubarrayProd(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(sum_Of_Subarray_Prod([1, 2, 3, 4, 5], 3), 15)
        self.assertEqual(sum_Of_Subarray_Prod([0, 0, 0, 0, 0], 5), 0)
        self.assertEqual(sum_Of_Subarray_Prod([-1, -2, -3, -4, -5], 3), -30)

    def test_edge_case_single_element(self):
        self.assertEqual(sum_Of_Subarray_Prod([1], 1), 1)

    def test_edge_case_empty_array(self):
        self.assertEqual(sum_Of_Subarray_Prod([], 1), 0)

    def test_edge_case_negative_n(self):
        self.assertEqual(sum_Of_Subarray_Prod([1, 2, 3], -1), 0)

    def test_corner_case_zero_product(self):
        self.assertEqual(sum_Of_Subarray_Prod([0, 0, 0], 3), 0)
