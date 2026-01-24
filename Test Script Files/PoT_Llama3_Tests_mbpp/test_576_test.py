import unittest
from mbpp_576_code import is_Sub_Array

class TestIsSubArray(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(is_Sub_Array([1, 2, 3, 4, 5], [2, 3], 5, 2))

    def test_edge_case1(self):
        self.assertFalse(is_Sub_Array([1, 2, 3, 4, 5], [6, 7], 5, 2))

    def test_edge_case2(self):
        self.assertTrue(is_Sub_Array([1, 2, 3, 4, 5], [1, 2], 5, 2))

    def test_edge_case3(self):
        self.assertTrue(is_Sub_Array([1, 2, 3, 4, 5], [1, 2, 3], 5, 3))

    def test_edge_case4(self):
        self.assertFalse(is_Sub_Array([1, 2, 3, 4, 5], [1, 2, 3, 4, 5], 5, 5))

    def test_edge_case5(self):
        self.assertFalse(is_Sub_Array([1, 2, 3, 4, 5], [], 5, 0))

    def test_edge_case6(self):
        self.assertFalse(is_Sub_Array([], [1, 2], 0, 2))

    def test_edge_case7(self):
        self.assertFalse(is_Sub_Array([1, 2, 3, 4, 5], [1, 2, 3, 4, 5, 6], 5, 6))

    def test_edge_case8(self):
        self.assertFalse(is_Sub_Array([1, 2, 3, 4, 5], [1, 2, 3, 4, 5, 6, 7], 5, 7))
