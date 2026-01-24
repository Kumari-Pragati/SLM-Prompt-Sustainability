import unittest
from mbpp_149_code import longest_subseq_with_diff_one

class TestLongestSubseqWithDiffOne(unittest.TestCase):

    def test_typical_case(self):
        arr = [5, 2, 9, 3, 6, 1, 10, 7]
        n = len(arr)
        self.assertEqual(longest_subseq_with_diff_one(arr, n), 4)

    def test_edge_case_single_element(self):
        arr = [5]
        n = len(arr)
        self.assertEqual(longest_subseq_with_diff_one(arr, n), 1)

    def test_edge_case_no_elements(self):
        arr = []
        n = len(arr)
        self.assertEqual(longest_subseq_with_diff_one(arr, n), 0)

    def test_edge_case_decreasing_sequence(self):
        arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        n = len(arr)
        self.assertEqual(longest_subseq_with_diff_one(arr, n), 1)

    def test_typical_case_with_duplicates(self):
        arr = [5, 2, 9, 3, 6, 1, 10, 7, 2, 9]
        n = len(arr)
        self.assertEqual(longest_subseq_with_diff_one(arr, n), 4)

    def test_typical_case_with_large_numbers(self):
        arr = [100, 99, 101, 98, 102, 97, 103]
        n = len(arr)
        self.assertEqual(longest_subseq_with_diff_one(arr, n), 4)
