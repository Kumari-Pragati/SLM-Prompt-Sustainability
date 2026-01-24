import unittest
from mbpp_938_code import find_closet

class TestFindCloset(unittest.TestCase):

    def test_typical_case(self):
        A = [1, 4, 5, 8]
        B = [2, 3, 6, 7]
        C = [3, 4, 5, 6]
        p = len(A)
        q = len(B)
        r = len(C)
        result = find_closet(A, B, C, p, q, r)
        self.assertEqual(result, (4, 3, 4))

    def test_edge_case_with_same_elements(self):
        A = [1, 1, 1]
        B = [1, 1, 1]
        C = [1, 1, 1]
        p = len(A)
        q = len(B)
        r = len(C)
        result = find_closet(A, B, C, p, q, r)
        self.assertEqual(result, (1, 1, 1))

    def test_edge_case_with_empty_lists(self):
        A = []
        B = []
        C = []
        p = len(A)
        q = len(B)
        r = len(C)
        result = find_closet(A, B, C, p, q, r)
        self.assertEqual(result, ())

    def test_error_case_with_different_lengths(self):
        A = [1, 2, 3]
        B = [4, 5]
        C = [6, 7, 8, 9]
        p = len(A)
        q = len(B)
        r = len(C)
        with self.assertRaises(IndexError):
            find_closet(A, B, C, p, q, r)
