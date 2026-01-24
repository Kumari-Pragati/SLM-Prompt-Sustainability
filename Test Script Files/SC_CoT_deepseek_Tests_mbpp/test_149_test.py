import unittest
from mbpp_149_code import longest_subseq_with_diff_one

class TestLongestSubseqWithDiffOne(unittest.TestCase):

    def test_typical_case(self):
        arr = [5, 2, 9, 3, 1, 10, 4, 6]
        n = len(arr)
        self.assertEqual(longest_subseq_with_diff_one(arr, n), 4)

    def test_edge_case(self):
        arr = [1, 2, 3, 4, 5]
        n = len(arr)
        self.assertEqual(longest_subseq_with_diff_one(arr, n), 5)

    def test_corner_case(self):
        arr = [1, 3, 5, 7, 9]
        n = len(arr)
        self.assertEqual(longest_subseq_with_diff_one(arr, n), 1)

    def test_invalid_input(self):
        arr = [1, 2, 'a', 4, 5]
        n = len(arr)
        with self.assertRaises(TypeError):
            longest_subseq_with_diff_one(arr, n)
