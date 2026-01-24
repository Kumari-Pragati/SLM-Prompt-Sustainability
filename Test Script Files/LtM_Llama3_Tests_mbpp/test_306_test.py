import unittest
from mbpp_306_code import max_sum_increasing_subseq

class TestMaxSumIncreasingSubseq(unittest.TestCase):
    def test_simple_case(self):
        self.assertEqual(max_sum_increasing_subseq([1, 2, 3], 3, 2, 1), 6)

    def test_edge_case(self):
        self.assertEqual(max_sum_increasing_subseq([1, 2, 3], 3, 0, 1), 3)

    def test_edge_case2(self):
        self.assertEqual(max_sum_increasing_subseq([1, 2, 3], 3, 2, 0), 3)

    def test_edge_case3(self):
        self.assertEqual(max_sum_increasing_subseq([1, 2, 3], 3, 1, 2), 4)

    def test_edge_case4(self):
        self.assertEqual(max_sum_increasing_subseq([1, 2, 3], 3, 0, 0), 1)

    def test_edge_case5(self):
        self.assertEqual(max_sum_increasing_subseq([1, 2, 3], 3, 2, 2), 6)

    def test_edge_case6(self):
        self.assertEqual(max_sum_increasing_subseq([1, 2, 3], 3, 1, 1), 3)

    def test_edge_case7(self):
        self.assertEqual(max_sum_increasing_subseq([1, 2, 3], 3, 0, 2), 3)

    def test_edge_case8(self):
        self.assertEqual(max_sum_increasing_subseq([1, 2, 3], 3, 2, 0), 3)

    def test_edge_case9(self):
        self.assertEqual(max_sum_increasing_subseq([1, 2, 3], 3, 1, 0), 2)

    def test_edge_case10(self):
        self.assertEqual(max_sum_increasing_subseq([1, 2, 3], 3, 0, 1), 3)

    def test_edge_case11(self):
        self.assertEqual(max_sum_increasing_subseq([1, 2, 3], 3, 2, 1), 6)

    def test_edge_case12(self):
        self.assertEqual(max_sum_increasing_subseq([1, 2, 3], 3, 1, 2), 4)

    def test_edge_case13(self):
        self.assertEqual(max_sum_increasing_subseq([1, 2, 3], 3, 0, 0), 1)

    def test_edge_case14(self):
        self.assertEqual(max_sum_increasing_subseq([1, 2, 3], 3, 2, 2), 6)

    def test_edge_case15(self):
        self.assertEqual(max_sum_increasing_subseq([1, 2, 3], 3, 1, 1), 3)

    def test_edge_case16(self):
        self.assertEqual(max_sum_increasing_subseq([1, 2, 3], 3, 0, 2), 3)

    def test_edge_case17(self):
        self.assertEqual(max_sum_increasing_subseq([1, 2, 3], 3, 2, 0), 3)

    def test_edge_case18(self):
        self.assertEqual(max_sum_increasing_subseq([1, 2, 3], 3, 1, 0), 2)

    def test_edge_case19(self):
        self.assertEqual(max_sum_increasing_subseq([1, 2, 3], 3, 0, 1), 3)

    def test_edge_case20(self):
        self.assertEqual(max_sum_increasing_subseq([1, 2, 3], 3, 2, 1), 6)
