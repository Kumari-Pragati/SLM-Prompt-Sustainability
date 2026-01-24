import unittest
from mbpp_149_code import longest_subseq_with_diff_one

class TestLongestSubseqWithDiffOne(unittest.TestCase):
    def test_typical_input(self):
        self.assertEqual(longest_subseq_with_diff_one([1, 2, 3, 4, 5], 5), 5)

    def test_edge_case(self):
        self.assertEqual(longest_subseq_with_diff_one([1, 2, 3, 4, 5, 6], 6), 6)

    def test_edge_case_reverse(self):
        self.assertEqual(longest_subseq_with_diff_one([6, 5, 4, 3, 2, 1], 6), 6)

    def test_edge_case_single_element(self):
        self.assertEqual(longest_subseq_with_diff_one([1], 1), 1)

    def test_edge_case_empty_list(self):
        self.assertEqual(longest_subseq_with_diff_one([], 0), 0)

    def test_edge_case_single_element_reverse(self):
        self.assertEqual(longest_subseq_with_diff_one([1], 1), 1)

    def test_edge_case_all_equal(self):
        self.assertEqual(longest_subseq_with_diff_one([1, 1, 1, 1, 1], 5), 1)

    def test_edge_case_all_equal_reverse(self):
        self.assertEqual(longest_subseq_with_diff_one([1, 1, 1, 1, 1], 5), 1)

    def test_edge_case_all_equal_reverse_reverse(self):
        self.assertEqual(longest_subseq_with_diff_one([1, 1, 1, 1, 1], 5), 1)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            longest_subseq_with_diff_one('abc', 5)
