import unittest
from mbpp_734_code import sum_Of_Subarray_Prod

class TestSumOfSubarrayProd(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(sum_Of_Subarray_Prod([1, 2, 3, 4], 1), 1)
        self.assertEqual(sum_Of_Subarray_Prod([1, 2, 3, 4], 2), 3)
        self.assertEqual(sum_Of_Subarray_Prod([1, 2, 3, 4], 3), 11)
        self.assertEqual(sum_Of_Subarray_Prod([1, 2, 3, 4], 4), 31)

    def test_empty_list(self):
        self.assertEqual(sum_Of_Subarray_Prod([], 1), 0)

    def test_single_element(self):
        self.assertEqual(sum_Of_Subarray_Prod([1], 1), 1)
        self.assertEqual(sum_Of_Subarray_Prod([1], 2), 1)

    def test_negative_numbers(self):
        self.assertEqual(sum_Of_Subarray_Prod([-1, -2, -3, -4], 1), -1)
        self.assertEqual(sum_Of_Subarray_Prod([-1, -2, -3, -4], 2), -3)
        self.assertEqual(sum_Of_Subarray_Prod([-1, -2, -3, -4], 3), 7)
        self.assertEqual(sum_Of_Subarray_Prod([-1, -2, -3, -4], 4), 23)

    def test_zero(self):
        self.assertEqual(sum_Of_Subarray_Prod([0], 1), 0)
        self.assertEqual(sum_Of_Subarray_Prod([0], 2), 0)

    def test_invalid_input_length(self):
        with self.assertRaises(ValueError):
            sum_Of_Subarray_Prod([1, 2, 3], 0)
        with self.assertRaises(ValueError):
            sum_Of_Subarray_Prod([1, 2, 3], 6)
