import unittest
from mbpp_863_code import find_longest_conseq_subseq

class TestFindLongestConseqSubseq(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(find_longest_conseq_subseq([1, 9, 3, 10, 4, 20, 2], 7), 4)

    def test_edge_case_single_element(self):
        self.assertEqual(find_longest_conseq_subseq([5], 1), 1)

    def test_edge_case_sorted_array(self):
        self.assertEqual(find_longest_conseq_subseq([1, 2, 3, 4, 5], 5), 5)

    def test_edge_case_unsorted_array(self):
        self.assertEqual(find_longest_conseq_subseq([1, 9, 3, 10, 4, 20, 2], 7), 4)

    def test_edge_case_duplicate_elements(self):
        self.assertEqual(find_longest_conseq_subseq([2, 2, 3, 4, 4, 4, 5, 6], 8), 3)

    def test_edge_case_consecutive_elements(self):
        self.assertEqual(find_longest_conseq_subseq([1, 2, 3, 4, 5, 6, 7, 8, 9], 9), 9)

    def test_edge_case_large_array(self):
        self.assertEqual(find_longest_conseq_subseq(list(range(1, 10001)), 10000), 10000)

    def test_invalid_input_empty_array(self):
        with self.assertRaises(Exception):
            find_longest_conseq_subseq([], 0)

    def test_invalid_input_negative_elements(self):
        with self.assertRaises(Exception):
            find_longest_conseq_subseq([-1, -9, -3, -10, -4, -20, -2], 7)
