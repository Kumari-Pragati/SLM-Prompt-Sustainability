import unittest
from mbpp_576_code import is_Sub_Array

class TestIsSubArray(unittest.TestCase):

    def test_empty_arrays(self):
        self.assertFalse(is_Sub_Array([], [], 0, 0))
        self.assertFalse(is_Sub_Array([], ["a"], 0, 1))
        self.assertFalse(is_Sub_Array(["a"], [], 1, 0))

    def test_single_element_arrays(self):
        self.assertFalse(is_Sub_Array([1], [2], 1, 1))
        self.assertTrue(is_Sub_Array([2], [2], 1, 1))
        self.assertFalse(is_Sub_Array(["a"], ["b"], 1, 1))
        self.assertTrue(is_Sub_Array(["b"], ["a"], 1, 1))

    def test_identical_arrays(self):
        self.assertTrue(is_Sub_Array([1, 2, 3], [1, 2, 3], 3, 3))
        self.assertTrue(is_Sub_Array(["a", "b", "c"], ["a", "b", "c"], 3, 3))

    def test_subarray_found_in_middle(self):
        self.assertTrue(is_Sub_Array([1, 2, 3, 4, 5], [3, 4], 5, 2))
        self.assertTrue(is_Sub_Array(["a", "b", "c", "d", "e"], ["c", "d"], 5, 2))

    def test_subarray_found_at_beginning(self):
        self.assertTrue(is_Sub_Array([1, 2, 3], [1, 2], 3, 2))
        self.assertTrue(is_Sub_Array(["a", "b", "c"], ["a", "b"], 3, 2))

    def test_subarray_found_at_end(self):
        self.assertTrue(is_Sub_Array([1, 2, 3, 4], [4], 4, 1))
        self.assertTrue(is_Sub_Array(["a", "b", "c", "d"], ["d"], 4, 1))

    def test_subarray_not_found(self):
        self.assertFalse(is_Sub_Array([1, 2, 3], [4], 3, 1))
        self.assertFalse(is_Sub_Array(["a", "b", "c"], ["d"], 3, 1))

    def test_negative_index(self):
        self.assertRaises(IndexError, is_Sub_Array, [1, 2, 3], [4], -1, 1)
        self.assertRaises(IndexError, is_Sub_Array, ["a", "b", "c"], ["d"], -1, 1)
