import unittest
from mbpp_149_code import longest_subseq_with_diff_one

class TestLongestSubseqWithDiffOne(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(longest_subseq_with_diff_one([10, 5, 9, 1, 11, 8, 6, 15, 3, 12, 2], 11), 5)

    def test_edge_case_single_element(self):
        self.assertEqual(longest_subseq_with_diff_one([5], 1), 1)

    def test_boundary_case_empty_array(self):
        self.assertEqual(longest_subseq_with_diff_one([], 0), 0)

    def test_corner_case_all_elements_diff_by_one(self):
        self.assertEqual(longest_subseq_with_diff_one([1, 2, 3, 4, 5], 5), 5)

    def test_corner_case_all_elements_same(self):
        self.assertEqual(longest_subseq_with_diff_one([1, 1, 1, 1, 1], 5), 1)

    def test_corner_case_elements_diff_by_two(self):
        self.assertEqual(longest_subseq_with_diff_one([1, 3, 5, 7, 9], 5), 1)

    def test_corner_case_elements_diff_by_more_than_one(self):
        self.assertEqual(longest_subseq_with_diff_one([10, 15, 20, 25, 30], 5), 1)
