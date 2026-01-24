import unittest
from mbpp_149_code import longest_subseq_with_diff_one

class TestLongestSubseqWithDiffOne(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(longest_subseq_with_diff_one([1, 2, 3, 4, 5], 5), 5)

    def test_edge_case(self):
        self.assertEqual(longest_subseq_with_diff_one([1, 2, 3, 5, 6], 5), 4)

    def test_edge_case2(self):
        self.assertEqual(longest_subseq_with_diff_one([1, 2, 3, 4, 5, 6], 6), 6)

    def test_edge_case3(self):
        self.assertEqual(longest_subseq_with_diff_one([1, 2, 3, 4, 5, 6, 7], 7), 6)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            longest_subseq_with_diff_one('abc', 5)

    def test_invalid_input2(self):
        with self.assertRaises(TypeError):
            longest_subseq_with_diff_one([1, 2, 3], 'abc')
