import unittest
from mbpp_938_code import find_closet

class TestFindCloset(unittest.TestCase):

    def test_typical(self):
        A = [1, 2, 3]
        B = [4, 5, 6]
        C = [7, 8, 9]
        p, q, r = len(A), len(B), len(C)
        expected = (1, 4, 7)
        self.assertEqual(find_closet(A, B, C, p, q, r), expected)

    def test_edge_case1(self):
        A = [1, 2, 3]
        B = [4, 5, 6]
        C = [7, 8, 9]
        p, q, r = len(A), len(B), len(C)
        expected = (1, 4, 7)
        self.assertEqual(find_closet(A, B, C, p, q, r), expected)

    def test_edge_case2(self):
        A = [1, 2, 3]
        B = [4, 5, 6]
        C = [7, 8, 9]
        p, q, r = len(A), len(B), len(C)
        expected = (1, 4, 7)
        self.assertEqual(find_closet(A, B, C, p, q, r), expected)

    def test_invalid_input1(self):
        A = [1, 2, 3]
        B = [4, 5, 6]
        C = [7, 8, 9]
        p, q, r = len(A), len(B), len(C)
        with self.assertRaises(TypeError):
            find_closet(A, B, C, p, q, 'r')

    def test_invalid_input2(self):
        A = [1, 2, 3]
        B = [4, 5, 6]
        C = [7, 8, 9]
        p, q, r = len(A), len(B), len(C)
        with self.assertRaises(TypeError):
            find_closet(A, B, C, p, 'q', r)

    def test_invalid_input3(self):
        A = [1, 2, 3]
        B = [4, 5, 6]
        C = [7, 8, 9]
        p, q, r = len(A), len(B), len(C)
        with self.assertRaises(TypeError):
            find_closet(A, B, C, p, q, r)
