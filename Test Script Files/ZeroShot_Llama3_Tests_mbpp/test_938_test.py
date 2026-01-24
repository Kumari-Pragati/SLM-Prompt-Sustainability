import unittest
from mbpp_938_code import find_closet

class TestFindCloset(unittest.TestCase):

    def test_find_closet(self):
        A = [1, 2, 3, 4, 5]
        B = [6, 7, 8, 9, 10]
        C = [11, 12, 13, 14, 15]
        p, q, r = 5, 5, 5
        expected_result = (1, 6, 11)
        self.assertEqual(find_closet(A, B, C, p, q, r), expected_result)

    def test_find_closet_empty(self):
        A = []
        B = []
        C = []
        p, q, r = 0, 0, 0
        with self.assertRaises(IndexError):
            find_closet(A, B, C, p, q, r)

    def test_find_closet_invalid_input(self):
        A = [1, 2, 3, 4, 5]
        B = [6, 7, 8, 9, 10]
        C = [11, 12, 13, 14, 15]
        p, q, r = -1, 5, 5
        with self.assertRaises(ValueError):
            find_closet(A, B, C, p, q, r)

    def test_find_closet_invalid_input2(self):
        A = [1, 2, 3, 4, 5]
        B = [6, 7, 8, 9, 10]
        C = [11, 12, 13, 14, 15]
        p, q, r = 5, -1, 5
        with self.assertRaises(ValueError):
            find_closet(A, B, C, p, q, r)

    def test_find_closet_invalid_input3(self):
        A = [1, 2, 3, 4, 5]
        B = [6, 7, 8, 9, 10]
        C = [11, 12, 13, 14, 15]
        p, q, r = 5, 5, -1
        with self.assertRaises(ValueError):
            find_closet(A, B, C, p, q, r)
