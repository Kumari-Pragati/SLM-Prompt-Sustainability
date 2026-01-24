import unittest
from mbpp_863_code import find_longest_conseq_subseq

class TestFindLongestConseqSubseq(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(find_longest_conseq_subseq([1, 13, 14, 15, 16, 17, 18, 19, 3, 4, 5, 6, 7, 8, 9], 19), 9)
        self.assertEqual(find_longest_conseq_subseq([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], 19), 19)
        self.assertEqual(find_longest_conseq_subseq([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20], 20), 20)

    def test_edge_case_single_element(self):
        self.assertEqual(find_longest_conseq_subseq([1], 1), 1)

    def test_edge_case_empty_list(self):
        self.assertEqual(find_longest_conseq_subseq([], 0), 0)

    def test_edge_case_decreasing_sequence(self):
        self.assertEqual(find_longest_conseq_subseq([19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1], 20), 1)

    def test_edge_case_increasing_then_decreasing(self):
        self.assertEqual(find_longest_conseq_subseq([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1], 20), 6)

    def test_edge_case_duplicates(self):
        self.assertEqual(find_longest_conseq_subseq([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10], 20), 8)
