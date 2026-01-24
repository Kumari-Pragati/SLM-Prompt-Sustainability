import unittest
from mbpp_863_code import find_longest_conseq_subseq

class TestFindLongestConseqSubseq(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(find_longest_conseq_subseq([1, 2, 3, 4, 5, 6, 7, 8, 9], 9), 9)

    def test_edge_case(self):
        self.assertEqual(find_longest_conseq_subseq([1, 2, 3, 5, 6, 7, 8, 9], 8), 4)

    def test_edge_case2(self):
        self.assertEqual(find_longest_conseq_subseq([1, 2, 3, 4, 5, 6, 7, 8], 8), 7)

    def test_edge_case3(self):
        self.assertEqual(find_longest_conseq_subseq([1, 2, 3, 4, 5, 6, 7], 7), 6)

    def test_edge_case4(self):
        self.assertEqual(find_longest_conseq_subseq([1, 2, 3, 4, 5], 5), 4)

    def test_edge_case5(self):
        self.assertEqual(find_longest_conseq_subseq([1, 2, 3], 3), 2)

    def test_edge_case6(self):
        self.assertEqual(find_longest_conseq_subseq([1, 2], 2), 1)

    def test_edge_case7(self):
        self.assertEqual(find_longest_conseq_subseq([1], 1), 1)

    def test_edge_case8(self):
        self.assertEqual(find_longest_conseq_subseq([], 0), 0)

    def test_edge_case9(self):
        self.assertEqual(find_longest_conseq_subseq([1], 1), 1)

    def test_edge_case10(self):
        self.assertEqual(find_longest_conseq_subseq([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10), 9)
