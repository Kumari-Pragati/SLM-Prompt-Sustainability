import unittest
from mbpp_576_code import is_Sub_Array

class TestIsSubArray(unittest.TestCase):
    def test_sub_array(self):
        self.assertTrue(is_Sub_Array([1, 2, 3, 4, 5], [1, 2, 3], 5, 3))

    def test_sub_array_edge(self):
        self.assertTrue(is_Sub_Array([1, 2, 3, 4, 5], [1, 2], 5, 2))

    def test_sub_array_empty(self):
        self.assertFalse(is_Sub_Array([1, 2, 3, 4, 5], [], 5, 0))

    def test_sub_array_non_sub(self):
        self.assertFalse(is_Sub_Array([1, 2, 3, 4, 5], [6, 7, 8], 5, 3))

    def test_sub_array_sub_array(self):
        self.assertTrue(is_Sub_Array([1, 2, 3, 4, 5, 6], [2, 3, 4], 6, 3))

    def test_sub_array_sub_array_edge(self):
        self.assertTrue(is_Sub_Array([1, 2, 3, 4, 5, 6], [2, 3], 6, 2))

    def test_sub_array_sub_array_empty(self):
        self.assertFalse(is_Sub_Array([1, 2, 3, 4, 5, 6], [], 6, 0))

    def test_sub_array_sub_array_non_sub(self):
        self.assertFalse(is_Sub_Array([1, 2, 3, 4, 5, 6], [7, 8, 9], 6, 3))
