import unittest
from mbpp_576_code import is_Sub_Array

class TestIsSubArray(unittest.TestCase):
    def test_empty_arrays(self):
        self.assertFalse(is_Sub_Array([], [], 0, 0))

    def test_single_element_arrays(self):
        self.assertTrue(is_Sub_Array([1], [1], 1, 1))
        self.assertFalse(is_Sub_Array([1], [2], 1, 1))

    def test_identical_arrays(self):
        self.assertTrue(is_Sub_Array([1, 2, 3], [1, 2, 3], 3, 3))

    def test_subarray_present(self):
        self.assertTrue(is_Sub_Array([1, 2, 3, 4, 5], [3, 4], 5, 2))
        self.assertTrue(is_Sub_Array([1, 2, 3, 4, 5], [3, 4, 5], 5, 3))

    def test_subarray_not_present(self):
        self.assertFalse(is_Sub_Array([1, 2, 3, 4, 5], [6, 7], 5, 2))

    def test_different_lengths(self):
        self.assertFalse(is_Sub_Array([1, 2, 3], [1, 2, 3, 4], 3, 4))
        self.assertFalse(is_Sub_Array([1, 2, 3], [1, 2], 3, 2))

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, is_Sub_Array, [1], [1, 2], 1, 2)
        self.assertRaises(TypeError, is_Sub_Array, [1], [1, 2], '3', 2)
        self.assertRaises(TypeError, is_Sub_Array, [1], [1, 2], 1, '2')
