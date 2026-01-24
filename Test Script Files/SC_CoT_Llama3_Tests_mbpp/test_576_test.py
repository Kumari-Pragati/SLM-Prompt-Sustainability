import unittest
from mbpp_576_code import is_Sub_Array

class TestIsSubArray(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(is_Sub_Array([1, 2, 3, 4, 5], [2, 3, 4], 5, 3))

    def test_edge_case1(self):
        self.assertFalse(is_Sub_Array([1, 2, 3, 4, 5], [2, 3, 4, 5], 5, 4))

    def test_edge_case2(self):
        self.assertTrue(is_Sub_Array([1, 2, 3, 4, 5], [1, 2, 3, 4, 5], 5, 5))

    def test_edge_case3(self):
        self.assertFalse(is_Sub_Array([1, 2, 3, 4, 5], [1, 2, 3, 4, 6], 5, 5))

    def test_special_case1(self):
        self.assertTrue(is_Sub_Array([1, 2, 3, 4, 5], [1, 2, 3], 5, 3))

    def test_special_case2(self):
        self.assertFalse(is_Sub_Array([1, 2, 3, 4, 5], [1, 2, 3, 4, 5, 6], 5, 6))

    def test_invalid_input1(self):
        with self.assertRaises(TypeError):
            is_Sub_Array('a', [1, 2, 3, 4, 5], 5, 3)

    def test_invalid_input2(self):
        with self.assertRaises(TypeError):
            is_Sub_Array([1, 2, 3, 4, 5], 'b', 5, 3)

    def test_invalid_input3(self):
        with self.assertRaises(TypeError):
            is_Sub_Array([1, 2, 3, 4, 5], [1, 2, 3, 4, 5], 'c', 3)

    def test_invalid_input4(self):
        with self.assertRaises(TypeError):
            is_Sub_Array([1, 2, 3, 4, 5], [1, 2, 3, 4, 5], 5, 'd')
