import unittest
from mbpp_149_code import longest_subseq_with_diff_one

class TestLongestSubseqWithDiffOne(unittest.TestCase):
    def test_typical_use_case(self):
        arr = [1, 2, 3, 4, 5]
        n = len(arr)
        self.assertEqual(longest_subseq_with_diff_one(arr, n), 5)

    def test_edge_case(self):
        arr = [1, 2, 3]
        n = len(arr)
        self.assertEqual(longest_subseq_with_diff_one(arr, n), 3)

    def test_edge_case_with_repeated_elements(self):
        arr = [1, 2, 2, 3, 3]
        n = len(arr)
        self.assertEqual(longest_subseq_with_diff_one(arr, n), 4)

    def test_edge_case_with_single_element(self):
        arr = [1]
        n = len(arr)
        self.assertEqual(longest_subseq_with_diff_one(arr, n), 1)

    def test_edge_case_with_empty_array(self):
        arr = []
        n = len(arr)
        self.assertEqual(longest_subseq_with_diff_one(arr, n), 0)
