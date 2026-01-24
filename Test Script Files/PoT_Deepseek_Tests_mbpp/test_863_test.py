import unittest
from mbpp_863_code import find_longest_conseq_subseq

class TestFindLongestConseqSubseq(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(find_longest_conseq_subseq([1, 9, 3, 10, 4, 20, 2], 7), 4)

    def test_edge_case_single_element(self):
        self.assertEqual(find_longest_conseq_subseq([5], 1), 1)

    def test_boundary_case_empty_array(self):
        self.assertEqual(find_longest_conseq_subseq([], 0), 0)

    def test_corner_case_repeated_elements(self):
        self.assertEqual(find_longest_conseq_subseq([1, 1, 1, 1], 4), 1)

    def test_corner_case_consecutive_elements(self):
        self.assertEqual(find_longest_conseq_subseq([1, 2, 3, 4, 5], 5), 5)

    def test_corner_case_non_consecutive_elements(self):
        self.assertEqual(find_longest_conseq_subseq([1, 3, 5, 7, 9], 5), 1)
