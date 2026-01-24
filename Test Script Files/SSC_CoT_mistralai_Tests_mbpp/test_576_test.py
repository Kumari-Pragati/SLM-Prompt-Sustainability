import unittest
from mbpp_576_code import is_Sub_Array

class TestIsSubArray(unittest.TestCase):

    def test_normal_case(self):
        self.assertTrue(is_Sub_Array([1, 2, 3, 2, 3], [2, 3], 5, 2))
        self.assertTrue(is_Sub_Array([1, 2, 3, 2, 3], [3, 2], 5, 2))
        self.assertTrue(is_Sub_Array([1, 1, 1, 1, 1], [1], 5, 1))

    def test_edge_cases(self):
        self.assertFalse(is_Sub_Array([1, 2, 3], [2, 3], 3, 2))
        self.assertFalse(is_Sub_Array([1, 2, 3], [3, 2], 3, 1))
        self.assertFalse(is_Sub_Array([1, 2, 3], [2, 3], 3, 0))
        self.assertFalse(is_Sub_Array([1, 2, 3], [2, 3], 0, 2))
        self.assertFalse(is_Sub_Array([], [2, 3], 0, 2))
        self.assertFalse(is_Sub_Array([1, 2, 3], [], 3, 2))

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, is_Sub_Array, [1, 2, 3], 'B', 3, 2)
        self.assertRaises(TypeError, is_Sub_Array, [1, 2, 3], [2, 3], -1, 2)
        self.assertRaises(TypeError, is_Sub_Array, [1, 2, 3], [2, 3], 3, -1)
