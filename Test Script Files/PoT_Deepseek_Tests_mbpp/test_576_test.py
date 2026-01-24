import unittest
from mbpp_576_code import is_Sub_Array

class TestIsSubArray(unittest.TestCase):

    def test_typical_case(self):
        A = [1, 2, 3, 4, 5]
        B = [2, 3, 4]
        self.assertTrue(is_Sub_Array(A, B, len(A), len(B)))

    def test_edge_case_empty_arrays(self):
        A = []
        B = []
        self.assertTrue(is_Sub_Array(A, B, len(A), len(B)))

    def test_boundary_case_same_arrays(self):
        A = [1, 2, 3]
        B = [1, 2, 3]
        self.assertTrue(is_Sub_Array(A, B, len(A), len(B)))

    def test_corner_case_subarray_at_start(self):
        A = [1, 2, 3, 4, 5]
        B = [1, 2]
        self.assertTrue(is_Sub_Array(A, B, len(A), len(B)))

    def test_corner_case_subarray_at_end(self):
        A = [1, 2, 3, 4, 5]
        B = [4, 5]
        self.assertTrue(is_Sub_Array(A, B, len(A), len(B)))

    def test_corner_case_subarray_in_middle(self):
        A = [1, 2, 3, 4, 5]
        B = [2, 3]
        self.assertTrue(is_Sub_Array(A, B, len(A), len(B)))

    def test_corner_case_non_existing_subarray(self):
        A = [1, 2, 3, 4, 5]
        B = [6, 7]
        self.assertFalse(is_Sub_Array(A, B, len(A), len(B)))
