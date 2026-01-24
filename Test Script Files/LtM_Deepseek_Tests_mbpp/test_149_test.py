import unittest
from mbpp_149_code import longest_subseq_with_diff_one

class TestLongestSubseqWithDiffOne(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(longest_subseq_with_diff_one([1, 2, 3, 4], 4), 4)
        self.assertEqual(longest_subseq_with_diff_one([1, 1, 1, 1], 4), 1)
        self.assertEqual(longest_subseq_with_diff_one([5, 4, 3, 2], 4), 4)

    def test_edge_conditions(self):
        self.assertEqual(longest_subseq_with_diff_one([], 0), 0)
        self.assertEqual(longest_subseq_with_diff_one([1], 1), 1)
        self.assertEqual(longest_subseq_with_diff_one([1, 2], 2), 2)

    def test_boundary_conditions(self):
        self.assertEqual(longest_subseq_with_diff_one([1, 2, 3, 4, 5], 5), 5)
        self.assertEqual(longest_subseq_with_diff_one([5, 4, 3, 2, 1], 5), 5)
        self.assertEqual(longest_subseq_with_diff_one([1, 3, 5, 7, 9], 5), 5)

    def test_complex_cases(self):
        self.assertEqual(longest_subseq_with_diff_one([1, 2, 3, 4, 6, 7, 8, 9], 8), 5)
        self.assertEqual(longest_subseq_with_diff_one([1, 2, 2, 3, 3, 4, 4, 5], 8), 5)
        self.assertEqual(longest_subseq_with_diff_one([5, 4, 3, 2, 1, 2, 3, 4], 8), 5)
