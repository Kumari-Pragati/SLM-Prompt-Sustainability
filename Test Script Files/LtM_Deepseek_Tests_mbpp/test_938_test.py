import unittest
from mbpp_938_code import find_closet

class TestFindCloset(unittest.TestCase):

    def test_simple_inputs(self):
        A = [1, 2, 3]
        B = [4, 5, 6]
        C = [7, 8, 9]
        self.assertEqual(find_closet(A, B, C, 3, 3, 3), (1, 4, 7))

    def test_edge_conditions(self):
        A = [1]
        B = [2]
        C = [3]
        self.assertEqual(find_closet(A, B, C, 1, 1, 1), (1, 2, 3))

        A = []
        B = [2, 3]
        C = [4, 5]
        self.assertEqual(find_closet(A, B, C, 0, 2, 2), (None, None, None))

    def test_boundary_conditions(self):
        A = [1, 2, 3, 4, 5]
        B = [6, 7, 8, 9, 10]
        C = [11, 12, 13, 14, 15]
        self.assertEqual(find_closet(A, B, C, 5, 5, 5), (1, 6, 11))

        A = [1, 2, 3, 4, 5]
        B = [6, 7, 8, 9, 10]
        C = [15, 14, 13, 12, 11]
        self.assertEqual(find_closet(A, B, C, 5, 5, 5), (5, 10, 15))

    def test_complex_cases(self):
        A = [1, 2, 3, 4, 5]
        B = [6, 7, 8, 9, 10]
        C = [15, 14, 13, 12, 11]
        self.assertEqual(find_closet(A, B, C, 5, 5, 5), (1, 6, 11))

        A = [1, 2, 3, 4, 5]
        B = [10, 9, 8, 7, 6]
        C = [15, 14, 13, 12, 11]
        self.assertEqual(find_closet(A, B, C, 5, 5, 5), (5, 10, 15))
