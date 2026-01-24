import unittest
from mbpp_938_code import find_closet

class TestFindCloset(unittest.TestCase):
    def test_simple(self):
        A = [1, 2, 3]
        B = [4, 5, 6]
        C = [7, 8, 9]
        p, q, r = 3, 3, 3
        self.assertEqual(find_closet(A, B, C, p, q, r), (1, 4, 7))

    def test_edge(self):
        A = [1, 2, 3]
        B = [4, 5, 6]
        C = [7, 8, 9]
        p, q, r = 0, 0, 0
        self.assertEqual(find_closet(A, B, C, p, q, r), (None, None, None))

    def test_max_min(self):
        A = [1, 2, 3]
        B = [4, 5, 6]
        C = [7, 8, 9]
        p, q, r = 3, 3, 3
        self.assertEqual(find_closet(A, B, C, p, q, r), (1, 4, 7))

    def test_max_min_edge(self):
        A = [1, 2, 3]
        B = [4, 5, 6]
        C = [7, 8, 9]
        p, q, r = 0, 0, 0
        self.assertEqual(find_closet(A, B, C, p, q, r), (None, None, None))

    def test_invalid_input(self):
        A = [1, 2, 3]
        B = [4, 5, 6]
        C = [7, 8, 9]
        p, q, r = 'a', 'b', 'c'
        with self.assertRaises(TypeError):
            find_closet(A, B, C, p, q, r)
