import unittest
from mbpp_576_code import is_Sub_Array

class TestIsSubArray(unittest.TestCase):

    def test_is_sub_array_true(self):
        self.assertTrue(is_Sub_Array([1, 2, 3, 4, 5], [1, 2, 3], 5, 3))

    def test_is_sub_array_false(self):
        self.assertFalse(is_Sub_Array([1, 2, 3, 4, 5], [1, 2, 6], 5, 3))

    def test_is_sub_array_true_empty_subarray(self):
        self.assertTrue(is_Sub_Array([1, 2, 3, 4, 5], [], 5, 0))

    def test_is_sub_array_false_empty_mainarray(self):
        self.assertFalse(is_Sub_Array([], [1, 2, 3], 0, 3))

    def test_is_sub_array_true_subarray_at_end(self):
        self.assertTrue(is_Sub_Array([1, 2, 3, 4, 5, 6], [4, 5, 6], 6, 3))

    def test_is_sub_array_false_subarray_at_start(self):
        self.assertFalse(is_Sub_array([1, 2, 3, 4, 5], [5, 4, 3], 5, 3))

    def test_is_sub_array_true_subarray_in_middle(self):
        self.assertTrue(is_Sub_Array([1, 2, 3, 4, 5, 6, 7], [4, 5, 6], 7, 3))

    def test_is_sub_array_false_subarray_out_of_bounds(self):
        self.assertFalse(is_Sub_Array([1, 2, 3, 4, 5], [6, 7, 8], 5, 3))
