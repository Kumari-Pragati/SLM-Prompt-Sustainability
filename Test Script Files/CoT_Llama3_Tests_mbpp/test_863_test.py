import unittest
from mbpp_863_code import find_longest_conseq_subseq

class TestFindLongestConseqSubseq(unittest.TestCase):

    def test_empty_array(self):
        self.assertEqual(find_longest_conseq_subseq([], 0), 0)

    def test_single_element_array(self):
        self.assertEqual(find_longest_conseq_subseq([1], 1), 1)

    def test_consecutive_elements(self):
        self.assertEqual(find_longest_conseq_subseq([1, 2, 3, 4, 5], 5), 5)

    def test_non_consecutive_elements(self):
        self.assertEqual(find_longest_conseq_subseq([1, 3, 5, 7, 9], 5), 1)

    def test_repeated_elements(self):
        self.assertEqual(find_longest_conseq_subseq([1, 2, 2, 3, 3, 3], 6), 3)

    def test_edge_case(self):
        self.assertEqual(find_longest_conseq_subseq([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10), 10)
