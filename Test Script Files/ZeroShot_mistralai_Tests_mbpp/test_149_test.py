import unittest
from mbpp_149_code import longest_subseq_with_diff_one

class TestLongestSubseqWithDiffOne(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(longest_subseq_with_diff_one([], 0), 0)

    def test_single_element(self):
        self.assertEqual(longest_subseq_with_diff_one([1], 1), 1)

    def test_two_elements(self):
        self.assertEqual(longest_subseq_with_diff_one([1, 2], 2), 2)

    def test_three_elements(self):
        self.assertEqual(longest_subseq_with_diff_one([1, 2, 3], 3), 3)

    def test_four_elements(self):
        self.assertEqual(longest_subseq_with_diff_one([1, 2, 3, 4], 4), 4)

    def test_five_elements(self):
        self.assertEqual(longest_subseq_with_diff_one([1, 2, 3, 4, 5], 5), 5)

    def test_duplicates(self):
        self.assertEqual(longest_subseq_with_diff_one([1, 1, 2, 3, 4, 4, 5], 7), 5)

    def test_negative_numbers(self):
        self.assertEqual(longest_subseq_with_diff_one([-1, -2, -3, -4, -5], 5), 1)

    def test_large_input(self):
        self.assertEqual(longest_subseq_with_diff_one([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], 15), 15)
