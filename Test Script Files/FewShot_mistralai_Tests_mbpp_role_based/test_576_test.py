import unittest
from mbpp_576_code import is_Sub_Array

class TestIsSubArray(unittest.TestCase):
    def test_sub_array_found(self):
        self.assertTrue(is_Sub_Array([1, 2, 3, 4, 5], [4, 5], 5, 2))
        self.assertTrue(is_Sub_Array([1, 2, 3, 4, 5], [4, 5, 6], 5, 3))

    def test_sub_array_not_found(self):
        self.assertFalse(is_Sub_Array([1, 2, 3, 4, 5], [6, 7, 8], 5, 3))
        self.assertFalse(is_Sub_Array([1, 2, 3, 4, 5], [1, 2, 3, 4, 5], 5, 5))

    def test_empty_arrays(self):
        self.assertFalse(is_Sub_Array([], [], 0, 0))
        self.assertFalse(is_Sub_Array([], [1], 0, 1))
        self.assertFalse(is_Sub_Array([1], [], 1, 0))

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            is_Sub_Array([1, 2, 3], [4, 5], -1, 2)
        with self.assertRaises(ValueError):
            is_Sub_Array([1, 2, 3], [4, 5], 1, -1)
