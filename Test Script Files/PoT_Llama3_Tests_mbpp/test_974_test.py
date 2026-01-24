import unittest
from mbpp_974_code import min_sum_path

class TestMinSumPath(unittest.TestCase):

    def test_typical_case(self):
        A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.assertEqual(min_sum_path(A), 1)

    def test_edge_case(self):
        A = [[1, 2, 3], [4, 5, 6]]
        self.assertEqual(min_sum_path(A), 1)

    def test_edge_case2(self):
        A = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
        self.assertEqual(min_sum_path(A), 1)

    def test_edge_case3(self):
        A = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
        self.assertEqual(min_sum_path(A), 1)

    def test_edge_case4(self):
        A = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]]
        self.assertEqual(min_sum_path(A), 1)

    def test_edge_case5(self):
        A = [[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12], [13, 14, 15, 16, 17, 18]]
        self.assertEqual(min_sum_path(A), 1)

    def test_edge_case6(self):
        A = [[1, 2, 3, 4, 5, 6, 7], [8, 9, 10, 11, 12, 13, 14], [15, 16, 17, 18, 19, 20, 21]]
        self.assertEqual(min_sum_path(A), 1)

    def test_edge_case7(self):
        A = [[1, 2, 3, 4, 5, 6, 7, 8], [9, 10, 11, 12, 13, 14, 15, 16], [17, 18, 19, 20, 21, 22, 23, 24]]
        self.assertEqual(min_sum_path(A), 1)

    def test_edge_case8(self):
        A = [[1, 2, 3, 4, 5, 6, 7, 8, 9], [10, 11, 12, 13, 14, 15, 16, 17, 18], [19, 20, 21, 22, 23, 24, 25, 26, 27]]
        self.assertEqual(min_sum_path(A), 1)

    def test_edge_case9(self):
        A = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [11, 12, 13, 14, 15, 16, 17, 18, 19, 20], [21, 22, 23, 24, 25, 26, 27, 28, 29, 30]]
        self.assertEqual(min_sum_path(A), 1)

    def test_edge_case10(self):
        A = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], [12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22], [23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]]
        self.assertEqual(min_sum_path(A), 1)
