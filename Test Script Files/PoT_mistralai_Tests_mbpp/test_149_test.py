import unittest
from mbpp_149_code import longest_subseq_with_diff_one

class TestLongestSubseqWithDiffOne(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(longest_subseq_with_diff_one([1, 2, 3, 4, 5], 5), 4)
        self.assertEqual(longest_subseq_with_diff_one([1, 2, 2, 3, 4, 5], 6), 4)
        self.assertEqual(longest_subseq_with_diff_one([1, 1, 2, 2, 3, 4, 5], 7), 4)
        self.assertEqual(longest_subseq_with_diff_one([1, 2, 3, 4, 5, 5, 6], 7), 5)

    def test_edge_and_boundary_cases(self):
        self.assertEqual(longest_subseq_with_diff_one([1, 1, 1, 1, 1], 5), 2)
        self.assertEqual(longest_subseq_with_diff_one([1, 2, 2, 2, 2], 5), 2)
        self.assertEqual(longest_subseq_with_diff_one([1, 2, 3, 3, 3], 5), 3)
        self.assertEqual(longest_subseq_with_diff_one([1, 2, 3, 4, 4, 4], 6), 3)
        self.assertEqual(longest_subseq_with_diff_one([1, 2, 3, 4, 5, 5], 6), 5)
        self.assertEqual(longest_subseq_with_diff_one([1, 1, 1, 1, 1, 1], 6), 1)
