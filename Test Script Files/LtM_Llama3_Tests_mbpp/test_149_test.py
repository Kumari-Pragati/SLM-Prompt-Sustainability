import unittest
from mbpp_149_code import longest_subseq_with_diff_one

class TestLongestSubseqWithDiffOne(unittest.TestCase):

    def test_empty_array(self):
        self.assertEqual(longest_subseq_with_diff_one([], 0), 0)

    def test_single_element_array(self):
        self.assertEqual(longest_subseq_with_diff_one([1], 1), 1)

    def test_two_elements_array(self):
        self.assertEqual(longest_subseq_with_diff_one([1, 2], 2), 1)

    def test_three_elements_array(self):
        self.assertEqual(longest_subseq_with_diff_one([1, 2, 3], 3), 1)

    def test_array_with_subsequence(self):
        self.assertEqual(longest_subseq_with_diff_one([1, 2, 3, 4, 5], 5), 5)

    def test_array_with_subsequence_and_gap(self):
        self.assertEqual(longest_subseq_with_diff_one([1, 2, 3, 4, 5, 6], 6), 6)

    def test_array_with_subsequence_and_gap_at_end(self):
        self.assertEqual(longest_subseq_with_diff_one([1, 2, 3, 4, 5, 6, 7], 7), 6)

    def test_array_with_subsequence_and_gap_at_start(self):
        self.assertEqual(longest_subseq_with_diff_one([2, 3, 4, 5, 6, 7], 6), 5)

    def test_array_with_subsequence_and_gap_at_start_and_end(self):
        self.assertEqual(longest_subseq_with_diff_one([2, 3, 4, 5, 6, 7, 8], 7), 5)

    def test_array_with_no_subsequence(self):
        self.assertEqual(longest_subseq_with_diff_one([1, 3, 5, 7], 4), 1)

    def test_array_with_no_subsequence_and_gap(self):
        self.assertEqual(longest_subseq_with_diff_one([1, 2, 4, 5, 7], 5), 1)

    def test_array_with_no_subsequence_and_gap_at_end(self):
        self.assertEqual(longest_subseq_with_diff_one([1, 2, 3, 5, 6, 7], 6), 1)

    def test_array_with_no_subsequence_and_gap_at_start(self):
        self.assertEqual(longest_subseq_with_diff_one([2, 3, 4, 5, 6, 7], 6), 1)

    def test_array_with_no_subsequence_and_gap_at_start_and_end(self):
        self.assertEqual(longest_subseq_with_diff_one([2, 3, 4, 5, 6, 7, 8], 7), 1)
