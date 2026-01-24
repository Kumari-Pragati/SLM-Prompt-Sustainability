import unittest
from mbpp_938_code import find_closet

class TestFindCloset(unittest.TestCase):

    def test_typical_case(self):
        A = [1, 4, 5]
        B = [2, 3, 6]
        C = [3, 4, 7]
        p = q = r = 3
        self.assertEqual(find_closet(A, B, C, p, q, r), (4, 4, 4))

    def test_edge_case(self):
        A = [1, 2, 3]
        B = [4, 5, 6]
        C = [7, 8, 9]
        p = q = r = 3
        self.assertEqual(find_closet(A, B, C, p, q, r), (1, 4, 7))

    def test_boundary_case(self):
        A = [1, 2, 3, 4, 5]
        B = [6, 7, 8, 9, 10]
        C = [11, 12, 13, 14, 15]
        p = q = r = 5
        self.assertEqual(find_closet(A, B, C, p, q, r), (1, 6, 11))

    def test_invalid_input(self):
        A = [1, 2, 3]
        B = [4, 5]
        C = [7, 8, 9]
        p = 3
        q = 2
        r = 3
        with self.assertRaises(IndexError):
            find_closet(A, B, C, p, q, r)
