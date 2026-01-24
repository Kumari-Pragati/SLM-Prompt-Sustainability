import unittest
from mbpp_576_code import is_Sub_Array

class TestIsSubArray(unittest.TestCase):

    def test_typical_case(self):
        A = [1, 2, 3, 4, 5]
        B = [2, 3]
        self.assertTrue(is_Sub_Array(A, B, len(A), len(B)))

    def test_edge_case_subarray_at_start(self):
        A = [1, 2, 3, 4, 5]
        B = [1, 2]
        self.assertTrue(is_Sub_Array(A, B, len(A), len(B)))

    def test_edge_case_subarray_at_end(self):
        A = [1, 2, 3, 4, 5]
        B = [4, 5]
        self.assertTrue(is_Sub_Array(A, B, len(A), len(B)))

    def test_edge_case_subarray_not_present(self):
        A = [1, 2, 3, 4, 5]
        B = [6, 7]
        self.assertFalse(is_Sub_Array(A, B, len(A), len(B)))

    def test_edge_case_empty_subarray(self):
        A = [1, 2, 3, 4, 5]
        B = []
        self.assertTrue(is_Sub_Array(A, B, len(A), len(B)))

    def test_edge_case_empty_array(self):
        A = []
        B = [1, 2, 3]
        self.assertFalse(is_Sub_Array(A, B, len(A), len(B)))

    def test_edge_case_identical_arrays(self):
        A = [1, 2, 3, 4, 5]
        B = [1, 2, 3, 4, 5]
        self.assertTrue(is_Sub_Array(A, B, len(A), len(B)))
