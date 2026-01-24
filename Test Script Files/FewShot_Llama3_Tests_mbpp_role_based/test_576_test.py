import unittest
from mbpp_576_code import is_Sub_Array

class TestIsSubArray(unittest.TestCase):
    def test_subarray_found(self):
        A = [1, 2, 3, 4, 5, 6]
        B = [2, 3, 4]
        n = len(A)
        m = len(B)
        self.assertTrue(is_Sub_Array(A, B, n, m))

    def test_subarray_not_found(self):
        A = [1, 2, 3, 4, 5, 6]
        B = [7, 8, 9]
        n = len(A)
        m = len(B)
        self.assertFalse(is_Sub_Array(A, B, n, m))

    def test_subarray_found_at_start(self):
        A = [1, 2, 3, 4, 5, 6]
        B = [1, 2]
        n = len(A)
        m = len(B)
        self.assertTrue(is_Sub_Array(A, B, n, m))

    def test_subarray_found_at_end(self):
        A = [1, 2, 3, 4, 5, 6]
        B = [5, 6]
        n = len(A)
        m = len(B)
        self.assertTrue(is_Sub_Array(A, B, n, m))

    def test_subarray_found_multiple_times(self):
        A = [1, 2, 3, 4, 5, 6, 2, 3, 4]
        B = [2, 3, 4]
        n = len(A)
        m = len(B)
        self.assertTrue(is_Sub_Array(A, B, n, m))

    def test_empty_subarray(self):
        A = [1, 2, 3, 4, 5, 6]
        B = []
        n = len(A)
        m = len(B)
        self.assertFalse(is_Sub_Array(A, B, n, m))

    def test_subarray_longer_than_original_array(self):
        A = [1, 2, 3]
        B = [1, 2, 3, 4, 5]
        n = len(A)
        m = len(B)
        self.assertFalse(is_Sub_Array(A, B, n, m))
