import unittest
from mbpp_938_code import find_closet

class TestFindCloset(unittest.TestCase):

    def test_find_closet(self):
        A = [1, 4, 5]
        B = [2, 3, 6]
        C = [3, 4, 7]
        p = len(A)
        q = len(B)
        r = len(C)
        result = find_closet(A, B, C, p, q, r)
        self.assertEqual(result, (4, 3, 4))

        A = [1, 2, 3]
        B = [4, 5, 6]
        C = [7, 8, 9]
        p = len(A)
        q = len(B)
        r = len(C)
        result = find_closet(A, B, C, p, q, r)
        self.assertEqual(result, (1, 4, 7))

        A = [10, 20, 30]
        B = [15, 25, 35]
        C = [20, 30, 40]
        p = len(A)
        q = len(B)
        r = len(C)
        result = find_closet(A, B, C, p, q, r)
        self.assertEqual(result, (10, 15, 20))
