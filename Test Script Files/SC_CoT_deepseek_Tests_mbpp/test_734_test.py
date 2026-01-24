import unittest
from mbpp_734_code import sum_Of_Subarray_Prod

class TestSumOfSubarrayProd(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(sum_Of_Subarray_Prod([1, 2, 3, 4], 4), 50)

    def test_edge_case_single_element(self):
        self.assertEqual(sum_Of_Subarray_Prod([5], 1), 5)

    def test_edge_case_empty_array(self):
        self.assertEqual(sum_Of_Subarray_Prod([], 0), 0)

    def test_corner_case_negative_numbers(self):
        self.assertEqual(sum_Of_Subarray_Prod([-1, -2, -3, -4], 4), -50)

    def test_corner_case_large_numbers(self):
        self.assertEqual(sum_Of_Subarray_Prod([10**6, 2*10**6, 3*10**6, 4*10**6], 4), 5*10**12)

    def test_invalid_input_non_integer_array(self):
        with self.assertRaises(TypeError):
            sum_Of_Subarray_Prod([1, 2, '3', 4], 4)

    def test_invalid_input_negative_size(self):
        with self.assertRaises(ValueError):
            sum_Of_Subarray_Prod([1, 2, 3, 4], -1)
