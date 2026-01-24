import unittest
from mbpp_938_code import find_closet

class TestFindCloset(unittest.TestCase):

    def test_typical_case(self):
        A = [1, 2, 3]
        B = [4, 5, 6]
        C = [7, 8, 9]
        p, q, r = 3, 3, 3
        result = find_closet(A, B, C, p, q, r)
        self.assertEqual(result, (1, 4, 7))

    def test_edge_case(self):
        A = [1, 2, 3]
        B = [4, 5, 6]
        C = [7, 8, 9]
        p, q, r = 1, 1, 1
        result = find_closet(A, B, C, p, q, r)
        self.assertEqual(result, (1, 4, 7))

    def test_error_case(self):
        A = [1, 2, 3]
        B = [4, 5, 6]
        C = [7, 8, 9]
        p, q, r = 0, 0, 0
        with self.assertRaises(IndexError):
            find_closet(A, B, C, p, q, r)

    def test_empty_list(self):
        A = []
        B = []
        C = []
        p, q, r = 0, 0, 0
        with self.assertRaises(IndexError):
            find_closet(A, B, C, p, q, r)
