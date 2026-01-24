import unittest
from mbpp_863_code import find_longest_conseq_subseq

class TestFindLongestConseqSubseq(unittest.TestCase):
    def test_empty_input(self):
        self.assertEqual(find_longest_conseq_subseq([], 0), 0)

    def test_single_element_input(self):
        self.assertEqual(find_longest_conseq_subseq([1], 1), 1)

    def test_two_consecutive_elements_input(self):
        self.assertEqual(find_longest_conseq_subseq([1, 2], 2), 2)

    def test_three_consecutive_elements_input(self):
        self.assertEqual(find_longest_conseq_subseq([1, 2, 3], 3), 3)

    def test_non_consecutive_elements_input(self):
        self.assertEqual(find_longest_conseq_subseq([1, 3, 5], 3), 1)

    def test_consecutive_elements_with_gaps_input(self):
        self.assertEqual(find_longest_conseq_subseq([1, 2, 4, 5], 4), 3)

    def test_consecutive_elements_with_gaps_and_duplicates_input(self):
        self.assertEqual(find_longest_conseq_subseq([1, 2, 2, 4, 5], 5), 3)

    def test_edge_case_input(self):
        self.assertEqual(find_longest_conseq_subseq([1, 2, 3, 4, 5, 6], 6), 6)

    def test_max_value_input(self):
        self.assertEqual(find_longest_conseq_subseq([100, 101, 102, 103, 104, 105], 6), 5)

    def test_min_value_input(self):
        self.assertEqual(find_longest_conseq_subseq([-100, -99, -98, -97, -96, -95], 6), 5)
