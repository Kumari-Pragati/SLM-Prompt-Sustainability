import unittest
from mbpp_938_code import find_closet

class TestFindCloset(unittest.TestCase):
    def test_typical_inputs(self):
        A = [1, 2, 3]
        B = [4, 5, 6]
        C = [7, 8, 9]
        p, q, r = 3, 3, 3
        expected = (1, 4, 7)
        self.assertEqual(find_closet(A, B, C, p, q, r), expected)

    def test_edge_case_p_zero(self):
        A = [1, 2, 3]
        B = [4, 5, 6]
        C = [7, 8, 9]
        p, q, r = 0, 3, 3
        with self.assertRaises(IndexError):
            find_closet(A, B, C, p, q, r)

    def test_edge_case_q_zero(self):
        A = [1, 2, 3]
        B = [4, 5, 6]
        C = [7, 8, 9]
        p, q, r = 3, 0, 3
        with self.assertRaises(IndexError):
            find_closet(A, B, C, p, q, r)

    def test_edge_case_r_zero(self):
        A = [1, 2, 3]
        B = [4, 5, 6]
        C = [7, 8, 9]
        p, q, r = 3, 3, 0
        with self.assertRaises(IndexError):
            find_closet(A, B, C, p, q, r)

    def test_edge_case_p_q_r_zero(self):
        A = [1, 2, 3]
        B = [4, 5, 6]
        C = [7, 8, 9]
        p, q, r = 0, 0, 0
        with self.assertRaises(IndexError):
            find_closet(A, B, C, p, q, r)

    def test_edge_case_p_zero_q_nonzero_r_nonzero(self):
        A = [1, 2, 3]
        B = [4, 5, 6]
        C = [7, 8, 9]
        p, q, r = 0, 3, 3
        with self.assertRaises(IndexError):
            find_closet(A, B, C, p, q, r)

    def test_edge_case_p_nonzero_q_zero_r_nonzero(self):
        A = [1, 2, 3]
        B = [4, 5, 6]
        C = [7, 8, 9]
        p, q, r = 3, 0, 3
        with self.assertRaises(IndexError):
            find_closet(A, B, C, p, q, r)

    def test_edge_case_p_nonzero_q_nonzero_r_zero(self):
        A = [1, 2, 3]
        B = [4, 5, 6]
        C = [7, 8, 9]
        p, q, r = 3, 3, 0
        with self.assertRaises(IndexError):
            find_closet(A, B, C, p, q, r)

    def test_edge_case_p_nonzero_q_nonzero_r_nonzero(self):
        A = [1, 2, 3]
        B = [4, 5, 6]
        C = [7, 8, 9]
        p, q, r = 3, 3, 3
        expected = (1, 4, 7)
        self.assertEqual(find_closet(A, B, C, p, q, r), expected)
