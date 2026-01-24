import unittest
from mbpp_734_code import sum_Of_Subarray_Prod

class TestSumOfSubarrayProd(unittest.TestCase):

    def test_typical_input(self):
        self.assertEqual(sum_Of_Subarray_Prod([1, 2, 3, 4, 5], 5), 15)
        self.assertEqual(sum_Of_Subarray_Prod([0, 0, 0, 0, 0], 5), 0)
        self.assertEqual(sum_Of_Subarray_Prod([10, 20, 30, 40, 50], 1), 10)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(sum_Of_Subarray_Prod([1], 1), 1)
        self.assertEqual(sum_Of_Subarray_Prod([1, 2], 2), 9)
        self.assertEqual(sum_Of_Subarray_Prod([1, 2, 3, 4, 5], 0), 0)
        self.assertEqual(sum_Of_Subarray_Prod([1, 2, 3, 4, 5], 6), 31)

    def test_negative_numbers(self):
        self.assertEqual(sum_Of_Subarray_Prod([-1, -2, 3, -4, 5], 3), -2)

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            sum_Of_Subarray_Prod([], 0)
        with self.assertRaises(ValueError):
            sum_Of_Subarray_Prod([1], -1)
