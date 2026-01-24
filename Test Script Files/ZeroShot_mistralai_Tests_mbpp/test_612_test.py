import unittest
from mbpp_612_code import merge

class TestMergeFunction(unittest.TestCase):

    def test_empty_lists(self):
        self.assertEqual(merge([]), [])
        self.assertEqual(merge([[], []]), [[]])

    def test_single_list(self):
        self.assertEqual(merge([[1, 2, 3]]), [[1, 2, 3]])

    def test_two_lists(self):
        self.assertEqual(merge([[1, 2], [3, 4]]), [[1, 3], [2, 4]])

    def test_multiple_lists(self):
        self.assertEqual(merge([[1, 2], [3, 4], [5, 6, 7]]), [[1, 3, 5], [2, 4, 6], [7]])

    def test_lists_with_different_lengths(self):
        self.assertEqual(merge([[1, 2], [3], [4, 5, 6]]), [[1, 3, 4], [2, None, 5], [None, None, 6]])
