import unittest
from mbpp_576_code import is_Sub_Array

class TestIsSubArray(unittest.TestCase):

    def test_sub_array_exists(self):
        A = [1, 2, 3, 4, 5]
        B = [2, 3, 4]
        self.assertTrue(is_Sub_Array(A, B, len(A), len(B)))

    def test_sub_array_does_not_exist(self):
        A = [1, 2, 3, 4, 5]
        B = [6, 7, 8]
        self.assertFalse(is_Sub_Array(A, B, len(A), len(B)))

    def test_empty_arrays(self):
        A = []
        B = []
        self.assertTrue(is_Sub_Array(A, B, len(A), len(B)))

    def test_single_element_arrays(self):
        A = [1]
        B = [1]
        self.assertTrue(is_Sub_Array(A, B, len(A), len(B)))

    def test_single_element_arrays_mismatch(self):
        A = [1]
        B = [2]
        self.assertFalse(is_Sub_Array(A, B, len(A), len(B)))
