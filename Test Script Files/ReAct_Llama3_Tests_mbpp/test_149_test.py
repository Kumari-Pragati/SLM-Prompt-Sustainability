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

    def test_four_elements_array(self):
        self.assertEqual(longest_subseq_with_diff_one([1, 2, 3, 4], 4), 1)

    def test_five_elements_array(self):
        self.assertEqual(longest_subseq_with_diff_one([1, 2, 3, 4, 5], 5), 1)

    def test_six_elements_array(self):
        self.assertEqual(longest_subseq_with_diff_one([1, 2, 3, 4, 5, 6], 6), 1)

    def test_seven_elements_array(self):
        self.assertEqual(longest_subseq_with_diff_one([1, 2, 3, 4, 5, 6, 7], 7), 1)

    def test_eight_elements_array(self):
        self.assertEqual(longest_subseq_with_diff_one([1, 2, 3, 4, 5, 6, 7, 8], 8), 1)

    def test_nine_elements_array(self):
        self.assertEqual(longest_subseq_with_diff_one([1, 2, 3, 4, 5, 6, 7, 8, 9], 9), 1)

    def test_tenth_elements_array(self):
        self.assertEqual(longest_subseq_with_diff_one([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10), 1)

    def test_array_with_subsequence(self):
        self.assertEqual(longest_subseq_with_diff_one([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], 11), 2)

    def test_array_with_subsequence_and_gap(self):
        self.assertEqual(longest_subseq_with_diff_one([1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 12], 11), 2)

    def test_array_with_subsequence_and_gap_at_end(self):
        self.assertEqual(longest_subseq_with_diff_one([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12], 11), 2)

    def test_array_with_subsequence_and_gap_at_start(self):
        self.assertEqual(longest_subseq_with_diff_one([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], 11), 2)

    def test_array_with_subsequence_and_gap_at_start_and_end(self):
        self.assertEqual(longest_subseq_with_diff_one([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], 11), 2)

    def test_array_with_subsequence_and_gap_at_start_and_end_and_middle(self):
        self.assertEqual(longest_subseq_with_diff_one([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], 12), 2)

    def test_array_with_subsequence_and_gap_at_start_and_end_and_middle_and_start(self):
        self.assertEqual(longest_subseq_with_diff_one([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14], 13), 2)

    def test_array_with_subsequence_and_gap_at_start_and_end_and_middle_and_start_and_end(self):
        self.assertEqual(longest_subseq_with_diff_one([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], 14), 2)

    def test_array_with_subsequence_and_gap_at_start_and_end_and_middle_and_start_and