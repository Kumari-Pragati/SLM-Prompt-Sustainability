import unittest
from mbpp_863_code import find_longest_conseq_subseq

class TestFindLongestConseqSubseq(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(find_longest_conseq_subseq([1, 2, 3, 4, 5, 6, 7, 8, 9], 9), 4)

    def test_edge_case1(self):
        self.assertEqual(find_longest_conseq_subseq([1, 2, 3, 5, 6, 7, 8, 9], 8), 4)

    def test_edge_case2(self):
        self.assertEqual(find_longest_conseq_subseq([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10), 5)

    def test_edge_case3(self):
        self.assertEqual(find_longest_conseq_subseq([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], 11), 5)

    def test_edge_case4(self):
        self.assertEqual(find_longest_conseq_subseq([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], 12), 6)

    def test_edge_case5(self):
        self.assertEqual(find_longest_conseq_subseq([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], 13), 6)

    def test_edge_case6(self):
        self.assertEqual(find_longest_conseq_subseq([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14], 14), 7)

    def test_edge_case7(self):
        self.assertEqual(find_longest_conseq_subseq([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], 15), 7)

    def test_edge_case8(self):
        self.assertEqual(find_longest_conseq_subseq([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], 16), 8)

    def test_edge_case9(self):
        self.assertEqual(find_longest_conseq_subseq([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17], 17), 8)

    def test_edge_case10(self):
        self.assertEqual(find_longest_conseq_subseq([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18], 18), 9)

    def test_edge_case11(self):
        self.assertEqual(find_longest_conseq_subseq([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], 19), 9)

    def test_edge_case12(self):
        self.assertEqual(find_longest_conseq_subseq([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20], 20), 10)

    def test_edge_case13(self):
        self.assertEqual(find_longest_conseq_subseq([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21], 21), 10)

    def test_edge_case14(self):
        self.assertEqual(find_longest_conseq_subseq([1, 2, 3, 4, 5, 6, 7, 8, 9, 10,