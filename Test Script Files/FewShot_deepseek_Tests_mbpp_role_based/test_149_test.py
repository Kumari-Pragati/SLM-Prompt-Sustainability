import unittest
from mbpp_149_code import longest_subseq_with_diff_one

class TestLongestSubseqWithDiffOne(unittest.TestCase):
    def test_typical_case(self):
        arr = [10, 5, 7, 8, 9]
        n = len(arr)
        self.assertEqual(longest_subseq_with_diff_one(arr, n), 3)

    def test_edge_case(self):
        arr = [1, 1, 1, 1, 1]
        n = len(arr)
        self.assertEqual(longest_subseq_with_diff_one(arr, n), 1)

    def test_boundary_case(self):
        arr = [10, 9, 8, 7, 6]
        n = len(arr)
        self.assertEqual(longest_subseq_with_diff_one(arr, n), 5)

    def test_invalid_input(self):
        arr = [10, 5, 7, 8, 9]
        n = -1
        with self.assertRaises(ValueError):
            longest_subseq_with_diff_one(arr, n)
