import unittest
from mbpp_938_code import find_closet

class TestFindCloset(unittest.TestCase):
    def test_typical_use_case(self):
        A = [1, 2, 3, 4, 5]
        B = [6, 7, 8, 9, 10]
        C = [11, 12, 13, 14, 15]
        p = 5
        q = 5
        r = 5
        result = find_closet(A, B, C, p, q, r)
        self.assertEqual(result, (1, 6, 11))

    def test_edge_case_p_q_r_zero(self):
        A = [1, 2, 3]
        B = [4, 5, 6]
        C = [7, 8, 9]
        p = 0
        q = 0
        r = 0
        with self.assertRaises(IndexError):
            find_closet(A, B, C, p, q, r)

    def test_edge_case_p_q_r_negative(self):
        A = [1, 2, 3]
        B = [4, 5, 6]
        C = [7, 8, 9]
        p = -1
        q = -1
        r = -1
        with self.assertRaises(IndexError):
            find_closet(A, B, C, p, q, r)

    def test_edge_case_p_q_r_large(self):
        A = [1, 2, 3]
        B = [4, 5, 6]
        C = [7, 8, 9]
        p = 100
        q = 100
        r = 100
        result = find_closet(A, B, C, p, q, r)
        self.assertEqual(result, (1, 4, 7))

    def test_invalid_input_type(self):
        A = [1, 2, 3]
        B = [4, 5, 6]
        C = [7, 8, 9]
        p = 'a'
        q = 'b'
        r = 'c'
        with self.assertRaises(TypeError):
            find_closet(A, B, C, p, q, r)
