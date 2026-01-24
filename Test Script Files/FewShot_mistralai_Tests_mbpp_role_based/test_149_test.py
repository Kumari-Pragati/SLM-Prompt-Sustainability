import unittest
from mbpp_149_code import longest_subseq_with_diff_one

class TestLongestSubseqWithDiffOne(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(longest_subseq_with_diff_one([1, 2, 3, 4, 5], 5), 3)
        self.assertEqual(longest_subseq_with_diff_one([1, 1, 1, 1, 1], 5), 1)
        self.assertEqual(longest_subseq_with_diff_one([1, 2, 3, 4, 5, 6], 6), 3)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(longest_subseq_with_diff_one([], 0), 0)
        self.assertEqual(longest_subseq_with_diff_one([1], 1), 1)
        self.assertEqual(longest_subseq_with_diff_one([1, 1], 2), 2)
        self.assertEqual(longest_subseq_with_diff_one([1, 2, 1], 3), 2)
        self.assertEqual(longest_subseq_with_diff_one([1, 2, 3, 2, 1], 5), 3)
        self.assertEqual(longest_subseq_with_diff_one([1, 2, 3, 4, 5, 4, 3, 2, 1], 9), 3)

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, longest_subseq_with_diff_one, [1, 2, 3], 'not_a_number')
        self.assertRaises(TypeError, longest_subseq_with_diff_one, [1, 2, 3], (1, 2, 3))
