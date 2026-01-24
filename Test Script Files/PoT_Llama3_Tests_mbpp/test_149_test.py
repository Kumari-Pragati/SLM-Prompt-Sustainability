import unittest
from mbpp_149_code import longest_subseq_with_diff_one

class TestLongestSubseqWithDiffOne(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(longest_subseq_with_diff_one([1, 2, 3, 4, 5], 5), 5)

    def test_edge_case(self):
        self.assertEqual(longest_subseq_with_diff_one([1, 2, 3, 4, 5, 6], 6), 6)

    def test_edge_case2(self):
        self.assertEqual(longest_subseq_with_diff_one([1, 2, 3, 4, 5, 7], 6), 4)

    def test_edge_case3(self):
        self.assertEqual(longest_subseq_with_diff_one([1, 2, 3, 4, 5, 6, 7], 7), 6)

    def test_edge_case4(self):
        self.assertEqual(longest_subseq_with_diff_one([1, 2, 3, 4, 5, 6, 7, 8], 8), 7)

    def test_edge_case5(self):
        self.assertEqual(longest_subseq_with_diff_one([1, 2, 3, 4, 5, 6, 7, 8, 9], 9), 8)

    def test_edge_case6(self):
        self.assertEqual(longest_subseq_with_diff_one([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10), 9)

    def test_edge_case7(self):
        self.assertEqual(longest_subseq_with_diff_one([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], 11), 9)

    def test_edge_case8(self):
        self.assertEqual(longest_subseq_with_diff_one([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], 12), 10)

    def test_edge_case9(self):
        self.assertEqual(longest_subseq_with_diff_one([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], 13), 11)

    def test_edge_case10(self):
        self.assertEqual(longest_subseq_with_diff_one([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14], 14), 12)

    def test_edge_case11(self):
        self.assertEqual(longest_subseq_with_diff_one([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], 15), 13)

    def test_edge_case12(self):
        self.assertEqual(longest_subseq_with_diff_one([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], 16), 14)

    def test_edge_case13(self):
        self.assertEqual(longest_subseq_with_diff_one([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17], 17), 15)

    def test_edge_case14(self):
        self.assertEqual(longest_subseq_with_diff_one([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18], 18), 16)

    def test_edge_case15(self):
        self.assertEqual(longest_subseq_with_diff_one([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], 19), 17)

    def test_edge_case16(self):
        self.assertEqual(longest_subseq_with_diff_one([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13