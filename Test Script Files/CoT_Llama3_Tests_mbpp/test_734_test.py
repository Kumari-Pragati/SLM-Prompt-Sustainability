import unittest
from mbpp_734_code import sum_Of_Subarray_Prod

class TestSum_Of_Subarray_Prod(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(sum_Of_Subarray_Prod([1, 2, 3, 4, 5], 5), 30)

    def test_edge_case_empty_array(self):
        self.assertEqual(sum_Of_Subarray_Prod([], 0), 0)

    def test_edge_case_single_element_array(self):
        self.assertEqual(sum_Of_Subarray_Prod([1], 1), 1)

    def test_edge_case_zero_length_array(self):
        self.assertEqual(sum_Of_Subarray_Prod([1, 2, 3], 0), 0)

    def test_invalid_input_non_integer_length(self):
        with self.assertRaises(TypeError):
            sum_Of_Subarray_Prod([1, 2, 3], 'a')

    def test_invalid_input_non_integer_array(self):
        with self.assertRaises(TypeError):
            sum_Of_Subarray_Prod('a', 5)

    def test_edge_case_negative_length(self):
        with self.assertRaises(ValueError):
            sum_Of_Subarray_Prod([1, 2, 3], -1)

    def test_edge_case_negative_array(self):
        with self.assertRaises(ValueError):
            sum_Of_Subarray_Prod([-1, -2, -3], 3)
