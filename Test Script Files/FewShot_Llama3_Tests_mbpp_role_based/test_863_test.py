import unittest
from mbpp_863_code import find_longest_conseq_subseq

class TestFindLongestConseqSubseq(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(find_longest_conseq_subseq([1, 2, 3, 4, 5, 7, 8, 9, 10, 11, 12], 12), 4)

    def test_edge_case_empty_array(self):
        self.assertEqual(find_longest_conseq_subseq([], 0), 0)

    def test_edge_case_single_element_array(self):
        self.assertEqual(find_longest_conseq_subseq([5], 1), 1)

    def test_edge_case_all_consecutive_elements(self):
        self.assertEqual(find_longest_conseq_subseq([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], 12), 11)

    def test_edge_case_no_consecutive_elements(self):
        self.assertEqual(find_longest_conseq_subseq([1, 3, 5, 7, 9, 11, 13], 7), 1)

    def test_edge_case_negative_numbers(self):
        self.assertEqual(find_longest_conseq_subseq([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12], 12), 4)

    def test_edge_case_duplicates(self):
        self.assertEqual(find_longest_conseq_subseq([1, 2, 2, 3, 4, 5, 5, 6, 7, 8, 9, 10, 11, 12], 12), 4)
