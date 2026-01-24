import unittest
from mbpp_576_code import is_Sub_Array

class TestIsSubArray(unittest.TestCase):

    def test_empty_arrays(self):
        self.assertFalse(is_Sub_Array([], [], 0, 0))
        self.assertFalse(is_Sub_Array([], [1], 0, 1))
        self.assertFalse(is_Sub_Array([1], [], 1, 0))

    def test_single_elements(self):
        self.assertFalse(is_Sub_Array([1], [2], 1, 1))
        self.assertTrue(is_Sub_Array([2], [1], 1, 1))

    def test_sub_array_present(self):
        self.assertTrue(is_Sub_Array([1, 2, 3, 2, 3], [2, 3], 5, 2))
        self.assertTrue(is_Sub_Array([1, 2, 3, 2, 3], [3, 2], 5, 2))
        self.assertTrue(is_Sub_Array([1, 2, 3, 2, 3], [1, 2], 5, 2))

    def test_sub_array_not_present(self):
        self.assertFalse(is_Sub_Array([1, 2, 3, 2, 3], [4, 5], 5, 2))
        self.assertFalse(is_Sub_Array([1, 2, 3, 2, 3], [6, 7], 5, 2))
        self.assertFalse(is_Sub_Array([1, 2, 3, 2, 3], [0, 1], 5, 2))

    def test_overlapping_sub_array(self):
        self.assertTrue(is_Sub_Array([1, 2, 3, 2, 3], [2, 3, 2], 5, 3))

    def test_different_lengths(self):
        self.assertFalse(is_Sub_Array([1, 2, 3], [1, 2], 3, 2))
        self.assertFalse(is_Sub_Array([1, 2, 3], [1, 2, 3, 4], 3, 3))
