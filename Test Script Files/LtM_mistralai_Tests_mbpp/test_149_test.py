import unittest
from mbpp_149_code import longest_subseq_with_diff_one

class TestLongestSubseqWithDiffOne(unittest.TestCase):

    def test_simple_case(self):
        self.assertEqual(longest_subseq_with_diff_one([1, 2, 3], 3), 3)
        self.assertEqual(longest_subseq_with_diff_one([1, 1, 1], 3), 2)
        self.assertEqual(longest_subseq_with_diff_one([1, 2, 1], 3), 2)

    def test_edge_case(self):
        self.assertEqual(longest_subseq_with_diff_one([1, 1], 2), 1)
        self.assertEqual(longest_subseq_with_diff_one([1, 2, 1, 2], 4), 3)
        self.assertEqual(longest_subseq_with_diff_one([2, 2, 2], 3), 1)

    def test_boundary_case(self):
        self.assertEqual(longest_subseq_with_diff_one([], 0), 0)
        self.assertEqual(longest_subseq_with_diff_one([1], 1), 1)
        self.assertEqual(longest_subseq_with_diff_one([1, 2, 3, 2, 1], 5), 4)
