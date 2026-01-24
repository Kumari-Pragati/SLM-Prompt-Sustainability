import unittest
from mbpp_149_code import longest_subseq_with_diff_one

class TestLongestSubseqWithDiffOne(unittest.TestCase):

    def test_longest_subseq_with_diff_one(self):
        self.assertEqual(longest_subseq_with_diff_one([1, 2, 3, 4, 5], 5), 5)
        self.assertEqual(longest_subseq_with_diff_one([1, 3, 5, 7, 9], 5), 5)
        self.assertEqual(longest_subseq_with_diff_one([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10), 10)
        self.assertEqual(longest_subseq_with_diff_one([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], 11), 10)
        self.assertEqual(longest_subseq_with_diff_one([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], 12), 11)
        self.assertEqual(longest_subseq_with_diff_one([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], 13), 12)
        self.assertEqual(longest_subseq_with_diff_one([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14], 14), 13)
        self.assertEqual(longest_subseq_with_diff_one([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], 15), 14)
        self.assertEqual(longest_subseq_with_diff_one([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], 16), 15)
        self.assertEqual(longest_subseq_with_diff_one([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17], 17), 16)
        self.assertEqual(longest_subseq_with_diff_one([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18], 18), 17)
        self.assertEqual(longest_subseq_with_diff_one([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], 19), 18)
        self.assertEqual(longest_subseq_with_diff_one([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20], 20), 19)
        self.assertEqual(longest_subseq_with_diff_one([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21], 21), 20)
        self.assertEqual(longest_subseq_with_diff_one([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22], 22), 21)
        self.assertEqual(longest_subseq_with_diff_one([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23], 23), 22)
        self.assertEqual(long