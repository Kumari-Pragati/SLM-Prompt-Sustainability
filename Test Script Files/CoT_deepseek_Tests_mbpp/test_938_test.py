import unittest
from mbpp_938_code import find_closet

class TestFindCloset(unittest.TestCase):

    def test_typical_case(self):
        A = [1, 4, 5]
        B = [2, 3, 6]
        C = [3, 4, 7]
        self.assertEqual(find_closet(A, B, C, len(A), len(B), len(C)), (4, 3, 4))

    def test_edge_case(self):
        A = [1, 2, 3]
        B = [4, 5, 6]
        C = [7, 8, 9]
        self.assertEqual(find_closet(A, B, C, len(A), len(B), len(C)), (1, 4, 7))

    def test_boundary_case(self):
        A = [10, 20, 30]
        B = [40, 50, 60]
        C = [70, 80, 90]
        self.assertEqual(find_closet(A, B, C, len(A), len(B), len(C)), (10, 40, 70))

    def test_invalid_input(self):
        A = [1, 2, 3]
        B = [4, 5, 6]
        C = [7, 8, 9]
        with self.assertRaises(TypeError):
            find_closet(A, B, 'C', len(A), len(B), len(C))
