import unittest
from mbpp_612_code import merge

class TestMerge(unittest.TestCase):
    def test_merge_two_lists(self):
        self.assertEqual(merge([[1, 2], [3, 4]]), [[1, 3], [2, 4]])

    def test_merge_three_lists(self):
        self.assertEqual(merge([[1, 2], [3, 4], [5, 6]]), [[1, 3, 5], [2, 4, 6]])

    def test_merge_empty_list(self):
        self.assertEqual(merge([]), [])

    def test_merge_single_list(self):
        self.assertEqual(merge([[1]]), [[1]])

    def test_merge_lists_with_different_lengths(self):
        self.assertEqual(merge([[1, 2], [3]]), [[1, 3], [2, None]])
