import unittest
from mbpp_612_code import merge

class TestMergeFunction(unittest.TestCase):

    def test_merge_empty_list(self):
        self.assertEqual(merge([]), [])

    def test_merge_single_element_list(self):
        self.assertEqual(merge([[1, 2, 3]]), [[1, 2, 3]])

    def test_merge_multiple_element_list(self):
        self.assertEqual(merge([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), [[1, 4, 7], [2, 5, 8], [3, 6, 9]])

    def test_merge_list_with_diff_length(self):
        self.assertEqual(merge([[1, 2, 3], [4, 5], [7, 8, 9, 10]]), [[1, 4, 7], [2, 5, 8], [3, 9, 10]])

    def test_merge_list_with_empty_sublist(self):
        self.assertEqual(merge([[1, 2, 3], [], [7, 8, 9]]), [[1, 7], [2, 8], [3, 9]])

    def test_merge_list_with_single_element_sublist(self):
        self.assertEqual(merge([[1, 2, 3], [4], [7, 8, 9]]), [[1, 4, 7], [2, 8], [3, 9]])
