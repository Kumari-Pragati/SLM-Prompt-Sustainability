import unittest
from mbpp_863_code import find_longest_conseq_subseq

class TestFindLongestConseqSubseq(unittest.TestCase):

    def test_typical_input(self):
        self.assertEqual(find_longest_conseq_subseq([1, 2, 3, 4, 5, 6, 7, 8, 9], 9), 9)

    def test_edge_case(self):
        self.assertEqual(find_longest_conseq_subseq([1, 2, 3, 4, 5], 5), 5)

    def test_edge_case2(self):
        self.assertEqual(find_longest_conseq_subseq([1, 2, 3, 5, 6, 7, 8, 9], 8), 7)

    def test_edge_case3(self):
        self.assertEqual(find_longest_conseq_subseq([1, 2, 3, 4, 5, 6, 7, 8], 7), 7)

    def test_edge_case4(self):
        self.assertEqual(find_longest_conseq_subseq([1, 2, 3, 5, 6, 7, 8, 9, 10], 9), 4)

    def test_edge_case5(self):
        self.assertEqual(find_longest_conseq_subseq([1, 2, 3, 5, 6, 7, 8, 9, 10, 11], 10), 4)

    def test_edge_case6(self):
        self.assertEqual(find_longest_conseq_subseq([1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 12], 11), 4)

    def test_edge_case7(self):
        self.assertEqual(find_longest_conseq_subseq([1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13], 12), 4)

    def test_edge_case8(self):
        self.assertEqual(find_longest_conseq_subseq([1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14], 13), 4)

    def test_edge_case9(self):
        self.assertEqual(find_longest_conseq_subseq([1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], 14), 4)

    def test_edge_case10(self):
        self.assertEqual(find_longest_conseq_subseq([1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], 15), 4)

    def test_edge_case11(self):
        self.assertEqual(find_longest_conseq_subseq([1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17], 16), 4)

    def test_edge_case12(self):
        self.assertEqual(find_longest_conseq_subseq([1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18], 17), 4)

    def test_edge_case13(self):
        self.assertEqual(find_longest_conseq_subseq([1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], 18), 4)

    def test_edge_case14(self):
        self.assertEqual(find_longest_conseq_subseq([1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20], 19), 4)

    def test_edge_case15(self):
        self.assertEqual(find_longest_conseq_subseq([1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21], 20), 4)