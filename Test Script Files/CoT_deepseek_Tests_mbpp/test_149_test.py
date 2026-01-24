import unittest
from mbpp_149_code import longest_subseq_with_diff_one

class TestLongestSubseqWithDiffOne(unittest.TestCase):

    def test_typical_case(self):
        arr = [10, 5, 7, 8, 9]
        n = len(arr)
        self.assertEqual(longest_subseq_with_diff_one(arr, n), 3)

    def test_edge_case_single_element(self):
        arr = [1]
        n = len(arr)
        self.assertEqual(longest_subseq_with_diff_one(arr, n), 1)

    def test_edge_case_empty_array(self):
        arr = []
        n = len(arr)
        self.assertEqual(longest_subseq_with_diff_one(arr, n), 0)

    def test_typical_case_with_duplicates(self):
        arr = [10, 5, 7, 8, 9, 9]
        n = len(arr)
        self.assertEqual(longest_subseq_with_diff_one(arr, n), 3)

    def test_typical_case_with_diff_two(self):
        arr = [10, 9, 8, 7, 6]
        n = len(arr)
        self.assertEqual(longest_subseq_with_diff_one(arr, n), 1)

    def test_invalid_input_negative_numbers(self):
        arr = [-1, -2, -3, -4]
        n = len(arr)
        with self.assertRaises(Exception):
            longest_subseq_with_diff_one(arr, n)

    def test_invalid_input_non_integer_elements(self):
        arr = [10, 5, '7', 8, 9]
        n = len(arr)
        with self.assertRaises(Exception):
            longest_subseq_with_diff_one(arr, n)
