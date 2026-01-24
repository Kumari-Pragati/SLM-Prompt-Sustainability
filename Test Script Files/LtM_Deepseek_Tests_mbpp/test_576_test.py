import unittest
from mbpp_576_code import is_Sub_Array

class TestIsSubArray(unittest.TestCase):

    def test_simple_case(self):
        A = [1, 2, 3, 4, 5]
        B = [1, 2, 3]
        self.assertTrue(is_Sub_Array(A, B, len(A), len(B)))

    def test_edge_case_empty_arrays(self):
        A = []
        B = []
        self.assertTrue(is_Sub_Array(A, B, len(A), len(B)))

    def test_edge_case_empty_B(self):
        A = [1, 2, 3, 4, 5]
        B = []
        self.assertFalse(is_Sub_Array(A, B, len(A), len(B)))

    def test_edge_case_empty_A(self):
        A = []
        B = [1, 2, 3]
        self.assertFalse(is_Sub_Array(A, B, len(A), len(B)))

    def test_boundary_case_same_elements(self):
        A = [1, 1, 1, 1, 1]
        B = [1, 1]
        self.assertTrue(is_Sub_Array(A, B, len(A), len(B)))

    def test_complex_case_different_elements(self):
        A = [1, 2, 3, 4, 5]
        B = [2, 3, 1]
        self.assertFalse(is_Sub_Array(A, B, len(A), len(B)))

    def test_complex_case_repeated_elements(self):
        A = [1, 2, 2, 3, 4, 2, 5]
        B = [2, 3]
        self.assertTrue(is_Sub_Array(A, B, len(A), len(B)))
