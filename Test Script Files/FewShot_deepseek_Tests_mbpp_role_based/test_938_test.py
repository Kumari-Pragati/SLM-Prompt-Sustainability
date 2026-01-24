import unittest
from mbpp_938_code import find_closet

class TestFindCloset(unittest.TestCase):
    def test_typical_case(self):
        A = [1, 4, 5]
        B = [2, 3, 6]
        C = [7, 8, 9]
        self.assertEqual(find_closet(A, B, C, len(A), len(B), len(C)), (1, 2, 7))

    def test_edge_case(self):
        A = [1]
        B = [2]
        C = [3]
        self.assertEqual(find_closet(A, B, C, len(A), len(B), len(C)), (1, 2, 3))

    def test_boundary_case(self):
        A = [1, 2, 3, 4, 5]
        B = [6, 7, 8, 9, 10]
        C = [11, 12, 13, 14, 15]
        self.assertEqual(find_closet(A, B, C, len(A), len(B), len(C)), (1, 6, 11))

    def test_invalid_input(self):
        A = [1, 2, 3]
        B = [4, 5]
        C = [6, 7, 8, 9]
        with self.assertRaises(IndexError):
            find_closet(A, B, C, len(A), len(B), len(C))
