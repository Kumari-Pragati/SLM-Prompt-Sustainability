import unittest
from mbpp_576_code import is_Sub_Array

class TestIsSubArray(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(is_Sub_Array([1, 2, 3, 2, 3], [2, 3], 5, 2))
        self.assertTrue(is_Sub_Array([1, 2, 3, 2, 3], [3, 2], 5, 2))
        self.assertTrue(is_Sub_Array([1, 2, 3, 2, 3], [1, 2], 5, 2))
        self.assertTrue(is_Sub_Array([1, 2, 3, 2, 3], [2], 5, 1))
        self.assertTrue(is_Sub_Array([1, 2, 3, 2, 3], [3], 5, 1))
        self.assertTrue(is_Sub_Array([1, 2, 3, 2, 3], [1], 5, 1))

    def test_edge_case(self):
        self.assertFalse(is_Sub_Array([], [], 0, 0))
        self.assertFalse(is_Sub_Array([1], [], 1, 0))
        self.assertFalse(is_Sub_Array([], [1], 0, 1))
        self.assertFalse(is_Sub_Array([1], [1, 2], 1, 2))
        self.assertFalse(is_Sub_Array([1, 2], [1], 2, 1))
        self.assertFalse(is_Sub_Array([1, 2], [1, 2, 3], 2, 3))

    def test_corner_case(self):
        self.assertTrue(is_Sub_Array([1, 1, 1], [1], 3, 1))
        self.assertTrue(is_Sub_Array([1, 1, 1, 1], [1], 4, 1))
        self.assertTrue(is_Sub_Array([1, 1, 1, 1], [1, 1], 4, 2))
        self.assertFalse(is_Sub_Array([1, 2, 1, 2], [1, 2], 4, 2))
        self.assertFalse(is_Sub_Array([1, 2, 1, 2], [2, 1], 4, 2))
