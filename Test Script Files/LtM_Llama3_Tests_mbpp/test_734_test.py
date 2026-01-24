import unittest
from mbpp_734_code import sum_Of_Subarray_Prod

class TestSum_Of_Subarray_Prod(unittest.TestCase):
    def test_empty_array(self):
        self.assertEqual(sum_Of_Subarray_Prod([], 0), 0)

    def test_single_element_array(self):
        self.assertEqual(sum_Of_Subarray_Prod([1], 1), 1)

    def test_two_elements_array(self):
        self.assertEqual(sum_Of_Subarray_Prod([1, 2], 2), 3)

    def test_negative_elements_array(self):
        self.assertEqual(sum_Of_Subarray_Prod([-1, -2], 2), -3)

    def test_positive_elements_array(self):
        self.assertEqual(sum_Of_Subarray_Prod([1, 2, 3], 3), 6)

    def test_zero_elements_array(self):
        self.assertEqual(sum_Of_Subarray_Prod([0, 0], 2), 0)

    def test_edge_case_array(self):
        self.assertEqual(sum_Of_Subarray_Prod([1, 2, 3, 4, 5], 5), 15)

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            sum_Of_Subarray_Prod("hello", 5)

    def test_invalid_input_length(self):
        with self.assertRaises(IndexError):
            sum_Of_Subarray_Prod([1, 2, 3], 0)
