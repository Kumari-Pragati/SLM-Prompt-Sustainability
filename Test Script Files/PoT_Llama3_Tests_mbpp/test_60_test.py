import unittest
from mbpp_60_code import max_len_sub

class TestMaxLenSub(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(max_len_sub([1, 2, 3, 4, 5], 5), 5)

    def test_edge_case(self):
        self.assertEqual(max_len_sub([1, 2, 3, 4, 5, 6], 6), 6)

    def test_edge_case2(self):
        self.assertEqual(max_len_sub([1, 2, 3, 4, 5, 6, 7], 7), 6)

    def test_edge_case3(self):
        self.assertEqual(max_len_sub([1, 2, 3, 4, 5, 6, 7, 8], 8), 6)

    def test_edge_case4(self):
        self.assertEqual(max_len_sub([1, 2, 3, 4, 5, 6, 7, 8, 9], 9), 6)

    def test_edge_case5(self):
        self.assertEqual(max_len_sub([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10), 6)

    def test_edge_case6(self):
        self.assertEqual(max_len_sub([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], 11), 6)

    def test_edge_case7(self):
        self.assertEqual(max_len_sub([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], 12), 6)

    def test_edge_case8(self):
        self.assertEqual(max_len_sub([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], 13), 6)

    def test_edge_case9(self):
        self.assertEqual(max_len_sub([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14], 14), 6)

    def test_edge_case10(self):
        self.assertEqual(max_len_sub([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], 15), 6)

    def test_edge_case11(self):
        self.assertEqual(max_len_sub([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], 16), 6)

    def test_edge_case12(self):
        self.assertEqual(max_len_sub([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17], 17), 6)

    def test_edge_case13(self):
        self.assertEqual(max_len_sub([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18], 18), 6)

    def test_edge_case14(self):
        self.assertEqual(max_len_sub([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], 19), 6)

    def test_edge_case15(self):
        self.assertEqual(max_len_sub([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20], 20), 6)

    def test_edge_case16(self):
        self.assertEqual(max_len_sub([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21], 21), 6)

    def