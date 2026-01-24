import unittest
from mbpp_90_code import len_log

class TestLenLog(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(len_log([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), 3)

    def test_edge_case(self):
        self.assertEqual(len_log([[], [1, 2, 3], [4, 5, 6]]), 3)

    def test_edge_case2(self):
        self.assertEqual(len_log([[1], [2, 3], [4, 5, 6]]), 3)

    def test_edge_case3(self):
        self.assertEqual(len_log([[1, 2], [3, 4, 5], [6, 7, 8, 9]]), 4)

    def test_edge_case4(self):
        self.assertEqual(len_log([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]), 5)

    def test_edge_case5(self):
        self.assertEqual(len_log([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]), 10)

    def test_edge_case6(self):
        self.assertEqual(len_log([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]]), 12)

    def test_edge_case7(self):
        self.assertEqual(len_log([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]]), 15)

    def test_edge_case8(self):
        self.assertEqual(len_log([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]]), 20)

    def test_edge_case9(self):
        self.assertEqual(len_log([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]]), 25)

    def test_edge_case10(self):
        self.assertEqual(len_log([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]]), 30)

    def test_edge_case11(self):
        self.assertEqual(len_log([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]]), 35)

    def test_edge_case12(self):
        self.assertEqual(len_log([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40]]), 40)

    def test_edge_case13(self):
        self.assertEqual(len_log([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29,