import unittest
from mbpp_576_code import is_Sub_Array

class TestIsSubArray(unittest.TestCase):

    def test_simple_match(self):
        self.assertTrue(is_Sub_Array([1, 2, 3, 2, 3], [2, 3], 5, 2))
        self.assertTrue(is_Sub_Array([4, 5, 6, 7, 8], [4, 5, 6], 5, 3))

    def test_empty_arrays(self):
        self.assertFalse(is_Sub_Array([], [], 0, 0))
        self.assertFalse(is_Sub_Array([], [1], 0, 1))
        self.assertFalse(is_Sub_Array([1], [], 1, 0))

    def test_single_element_match(self):
        self.assertTrue(is_Sub_Array([1], [1], 1, 1))
        self.assertFalse(is_Sub_Array([2], [1], 1, 1))

    def test_no_match(self):
        self.assertFalse(is_Sub_Array([1, 2, 3], [4, 5, 6], 3, 3))
        self.assertFalse(is_Sub_Array([1, 2, 3], [1, 4, 5], 3, 3))

    def test_edge_cases(self):
        self.assertTrue(is_Sub_Array([1, 2, 3], [2], 3, 1))
        self.assertTrue(is_Sub_Array([1, 2, 3], [2, 3], 3, 2))
        self.assertTrue(is_Sub_Array([1, 2, 3], [2, 3, 4], 3, 3))
        self.assertFalse(is_Sub_Array([1, 2, 3], [2, 3, 4], 3, 4))
