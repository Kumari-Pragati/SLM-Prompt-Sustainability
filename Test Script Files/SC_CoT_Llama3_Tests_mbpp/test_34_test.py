import unittest
from mbpp_34_code import find_missing

class TestFindMissing(unittest.TestCase):
    def test_typical_input(self):
        ar = [1, 2, 3, 5, 6, 7, 8, 9, 10]
        self.assertEqual(find_missing(ar, 10), 4)

    def test_edge_case(self):
        ar = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertEqual(find_missing(ar, 9), 10)

    def test_edge_case2(self):
        ar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertEqual(find_missing(ar, 10), -1)

    def test_edge_case3(self):
        ar = [1, 2, 3, 4, 5, 6, 7, 8]
        self.assertEqual(find_missing(ar, 8), 9)

    def test_edge_case4(self):
        ar = [1, 2, 3, 4, 5, 6, 7]
        self.assertEqual(find_missing(ar, 7), 8)

    def test_edge_case5(self):
        ar = [1, 2, 3, 4, 5, 6]
        self.assertEqual(find_missing(ar, 6), 7)

    def test_edge_case6(self):
        ar = [1, 2, 3, 4, 5]
        self.assertEqual(find_missing(ar, 5), 6)

    def test_edge_case7(self):
        ar = [1, 2, 3, 4]
        self.assertEqual(find_missing(ar, 4), 5)

    def test_edge_case8(self):
        ar = [1, 2, 3]
        self.assertEqual(find_missing(ar, 3), 4)

    def test_edge_case9(self):
        ar = [1, 2]
        self.assertEqual(find_missing(ar, 2), 3)

    def test_edge_case10(self):
        ar = [1]
        self.assertEqual(find_missing(ar, 1), 2)

    def test_edge_case11(self):
        ar = []
        self.assertEqual(find_missing(ar, 0), -1)

    def test_edge_case12(self):
        ar = [1]
        self.assertEqual(find_missing(ar, 1), -1)

    def test_edge_case13(self):
        ar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
        self.assertEqual(find_missing(ar, 20), -1)

    def test_edge_case14(self):
        ar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]
        self.assertEqual(find_missing(ar, 50), -1)

    def test_edge_case15(self):
        ar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60]
        self.assertEqual(find_missing(ar, 60), -1)

    def test_edge_case16(self):
        ar = [1, 2, 3, 4, 5, 6, 7, 8, 9