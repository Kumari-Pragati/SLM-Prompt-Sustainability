import unittest
from mbpp_612_code import merge

class TestMergeFunction(unittest.TestCase):

    def test_merge_with_single_list(self):
        self.assertEqual(merge([[1, 2, 3]]), [[1], [2], [3]])

    def test_merge_with_multiple_lists(self):
        self.assertEqual(merge([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), [[1, 4, 7], [2, 5, 8], [3, 6, 9]])

    def test_merge_with_empty_list(self):
        self.assertEqual(merge([]), [])

    def test_merge_with_single_element_list(self):
        self.assertEqual(merge([[1]]), [[1]])

    def test_merge_with_lists_of_different_lengths(self):
        self.assertEqual(merge([[1, 2, 3], [4, 5], [6, 7, 8, 9]]), [[1, 4, 6], [2, 5, 7], [3, 8, 9]])

    def test_merge_with_lists_of_zero_length(self):
        self.assertEqual(merge([[], [], []]), [])

    def test_merge_with_lists_of_one_element(self):
        self.assertEqual(merge([[1], [2], [3]]), [[1], [2], [3]])

    def test_merge_with_lists_of_empty_list(self):
        self.assertEqual(merge([[], [], []]), [])
