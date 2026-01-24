import unittest
from mbpp_149_code import longest_subseq_with_diff_one

class TestLongestSubseqWithDiffOne(unittest.TestCase):

    def test_longest_subseq_with_diff_one(self):
        self.assertEqual(longest_subseq_with_diff_one([10, 5, 7, 8, 9], 5), 3)
        self.assertEqual(longest_subseq_with_diff_one([1, 2, 3, 4, 5], 5), 5)
        self.assertEqual(longest_subseq_with_diff_one([1, 3, 5, 7, 9], 5), 1)
        self.assertEqual(longest_subseq_with_diff_one([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10), 10)
        self.assertEqual(longest_subseq_with_diff_one([10, 9, 8, 7, 6], 5), 1)
