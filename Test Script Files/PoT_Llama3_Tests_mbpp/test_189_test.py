import unittest
from mbpp_189_code import first_Missing_Positive

class TestFirstMissingPositive(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(first_Missing_Positive([1, 2, 3, 4, 5], 5), 6)

    def test_edge_case(self):
        self.assertEqual(first_Missing_Positive([1, 2, 3, 4, 6], 5), 5)

    def test_edge_case2(self):
        self.assertEqual(first_Missing_Positive([1, 2, 3, 4, 5, 7], 5), 6)

    def test_edge_case3(self):
        self.assertEqual(first_Missing_Positive([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10), 11)

    def test_edge_case4(self):
        self.assertEqual(first_Missing_Positive([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20], 20), 21)

    def test_edge_case5(self):
        self.assertEqual(first_Missing_Positive([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30], 30), 31)

    def test_edge_case6(self):
        self.assertEqual(first_Missing_Positive([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50], 50), 51)

    def test_edge_case7(self):
        self.assertEqual(first_Missing_Positive([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60], 60), 61)

    def test_edge_case8(self):
        self.assertEqual(first_Missing_Positive([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70], 70), 71)

    def test_edge_case9(self):
        self.assertEqual(first_Missing_Positive([1, 2, 3, 4, 5, 6, 7,