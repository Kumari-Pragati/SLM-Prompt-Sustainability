import unittest
from734_code import sum_Of_Subarray_Prod

class TestSumOfSubarrayProd(unittest.TestCase):
    def test_empty_array(self):
        self.assertEqual(sum_Of_Subarray_Prod([], 0), 0)

    def test_single_element_array(self):
        self.assertEqual(sum_Of_Subarray_Prod([1], 1), 1)

    def test_positive_array(self):
        self.assertEqual(sum_Of_Subarray_Prod([1, 2, 3, 4], 4), 30)
        self.assertEqual(sum_Of_Subarray_Prod([1, 2, 3, 4, 5], 5), 151)

    def test_negative_array(self):
        self.assertEqual(sum_Of_Subarray_Prod([-1, -2, -3, -4], 4), -30)
        self.assertEqual(sum_Of_Subarray_Prod([-1, -2, -3, -4, -5], 5), -151)

    def test_zero_element(self):
        self.assertEqual(sum_Of_Subarray_Prod([0], 1), 0)
        self.assertEqual(sum_Of_Subarray_Prod([0, 0], 2), 0)

    def test_negative_n(self):
        self.assertRaises(IndexError, lambda: sum_Of_Subarray_Prod([1, 2, 3], -1))
