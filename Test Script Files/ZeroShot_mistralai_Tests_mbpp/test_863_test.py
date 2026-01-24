import unittest
from mbpp_863_code import find_longest_conseq_subseq

class TestFindLongestConseqSubseq(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(find_longest_conseq_subseq([], 0), 0)

    def test_single_element_list(self):
        self.assertEqual(find_longest_conseq_subseq([1], 1), 1)

    def test_consecutive_elements_list(self):
        self.assertEqual(find_longest_conseq_subseq([1, 2, 3, 4, 5], 5), 5)

    def test_non_consecutive_elements_list(self):
        self.assertEqual(find_longest_conseq_subseq([1, 3, 5, 6, 7, 8, 9], 7), 6)

    def test_duplicate_elements_list(self):
        self.assertEqual(find_longest_conseq_subseq([1, 1, 2, 3, 4, 4, 5], 6), 4)

    def test_negative_numbers_list(self):
        self.assertEqual(find_longest_conseq_subseq([-1, -2, -3, -4, -5], 5), 5)

    def test_unsorted_list(self):
        self.assertEqual(find_longest_conseq_subseq([3, 4, 2, 1, 5, 6], 6), 6)
