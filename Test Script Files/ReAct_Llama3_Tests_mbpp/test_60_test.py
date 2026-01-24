import unittest
from mbpp_60_code import max_len_sub

class TestMaxLenSub(unittest.TestCase):

    def test_typical_case(self):
        arr = [1, 2, 3, 4, 5]
        n = len(arr)
        self.assertEqual(max_len_sub(arr, n), 5)

    def test_edge_case(self):
        arr = [1, 1, 1, 1, 1]
        n = len(arr)
        self.assertEqual(max_len_sub(arr, n), 1)

    def test_edge_case2(self):
        arr = [1, 2, 3, 4, 5, 6]
        n = len(arr)
        self.assertEqual(max_len_sub(arr, n), 6)

    def test_edge_case3(self):
        arr = [1, 2, 3, 4, 5, 6, 7]
        n = len(arr)
        self.assertEqual(max_len_sub(arr, n), 7)

    def test_edge_case4(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8]
        n = len(arr)
        self.assertEqual(max_len_sub(arr, n), 8)

    def test_edge_case5(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        n = len(arr)
        self.assertEqual(max_len_sub(arr, n), 9)

    def test_edge_case6(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        n = len(arr)
        self.assertEqual(max_len_sub(arr, n), 10)

    def test_edge_case7(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        n = len(arr)
        self.assertEqual(max_len_sub(arr, n), 11)

    def test_edge_case8(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        n = len(arr)
        self.assertEqual(max_len_sub(arr, n), 12)

    def test_edge_case9(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        n = len(arr)
        self.assertEqual(max_len_sub(arr, n), 13)

    def test_edge_case10(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
        n = len(arr)
        self.assertEqual(max_len_sub(arr, n), 14)

    def test_edge_case11(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        n = len(arr)
        self.assertEqual(max_len_sub(arr, n), 15)

    def test_edge_case12(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
        n = len(arr)
        self.assertEqual(max_len_sub(arr, n), 16)

    def test_edge_case13(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
        n = len(arr)
        self.assertEqual(max_len_sub(arr, n), 17)

    def test_edge_case14(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
        n = len(arr)
        self.assertEqual(max_len_sub(arr, n), 18)

    def test_edge_case15(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15