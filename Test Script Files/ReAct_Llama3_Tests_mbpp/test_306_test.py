import unittest
from mbpp_306_code import max_sum_increasing_subseq

class TestMaxSumIncreasingSubseq(unittest.TestCase):

    def test_typical_case(self):
        a = [1, 2, 3, 4, 5]
        n = len(a)
        index = 4
        k = 4
        self.assertEqual(max_sum_increasing_subseq(a, n, index, k), 15)

    def test_edge_case(self):
        a = [5, 4, 3, 2, 1]
        n = len(a)
        index = 4
        k = 4
        self.assertEqual(max_sum_increasing_subseq(a, n, index, k), 5)

    def test_edge_case2(self):
        a = [1, 1, 1, 1, 1]
        n = len(a)
        index = 4
        k = 4
        self.assertEqual(max_sum_increasing_subseq(a, n, index, k), 5)

    def test_edge_case3(self):
        a = [1, 2, 3, 4, 5]
        n = len(a)
        index = 0
        k = 0
        self.assertEqual(max_sum_increasing_subseq(a, n, index, k), 1)

    def test_edge_case4(self):
        a = [1, 2, 3, 4, 5]
        n = len(a)
        index = 4
        k = 0
        self.assertEqual(max_sum_increasing_subseq(a, n, index, k), 1)

    def test_edge_case5(self):
        a = [1, 2, 3, 4, 5]
        n = len(a)
        index = 0
        k = 4
        self.assertEqual(max_sum_increasing_subseq(a, n, index, k), 5)

    def test_edge_case6(self):
        a = [1, 2, 3, 4, 5]
        n = len(a)
        index = 4
        k = 4
        self.assertEqual(max_sum_increasing_subseq(a, n, index, k), 5)

    def test_edge_case7(self):
        a = [1, 2, 3, 4, 5]
        n = len(a)
        index = 0
        k = 0
        self.assertEqual(max_sum_increasing_subseq(a, n, index, k), 1)

    def test_edge_case8(self):
        a = [1, 2, 3, 4, 5]
        n = len(a)
        index = 4
        k = 0
        self.assertEqual(max_sum_increasing_subseq(a, n, index, k), 1)

    def test_edge_case9(self):
        a = [1, 2, 3, 4, 5]
        n = len(a)
        index = 0
        k = 4
        self.assertEqual(max_sum_increasing_subseq(a, n, index, k), 5)

    def test_edge_case10(self):
        a = [1, 2, 3, 4, 5]
        n = len(a)
        index = 4
        k = 4
        self.assertEqual(max_sum_increasing_subseq(a, n, index, k), 5)
