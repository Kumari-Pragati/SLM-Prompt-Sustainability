import unittest
from mbpp_149_code import longest_subseq_with_diff_one

class TestLongestSubseqWithDiffOne(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(longest_subseq_with_diff_one([1, 2, 3, 4, 5], 5), 4)
        self.assertEqual(longest_subseq_with_diff_one([1, 1, 2, 2, 3], 5), 3)
        self.assertEqual(longest_subseq_with_diff_one([1, 2, 3, 1, 2], 5), 3)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(longest_subseq_with_diff_one([1, 1, 1, 1], 4), 1)
        self.assertEqual(longest_subseq_with_diff_one([1, 2, 2, 3], 3), 2)
        self.assertEqual(longest_subseq_with_diff_one([1, 1, 1, 1, 1], 5), 1)
        self.assertEqual(longest_subseq_with_diff_one([1, 2, 3, 4, 5, 6], 6), 5)
        self.assertEqual(longest_subseq_with_diff_one([1, 2, 3, 4, 5, 6, 1], 7), 5)

    def test_special_cases(self):
        self.assertEqual(longest_subseq_with_diff_one([1, 1, 1], 3), 1)
        self.assertEqual(longest_subseq_with_diff_one([1, 2, 2, 2], 4), 2)
        self.assertEqual(longest_subseq_with_diff_one([1, 1, 2, 2, 2], 5), 3)
        self.assertEqual(longest_subseq_with_diff_one([2, 2, 2, 2, 1], 5), 3)
        self.assertEqual(longest_subseq_with_diff_one([2, 2, 2, 1, 1], 5), 2)
