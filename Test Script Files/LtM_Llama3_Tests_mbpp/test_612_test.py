import unittest
from mbpp_612_code import merge

class TestMerge(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(merge([]), [])

    def test_single_list(self):
        self.assertEqual(merge([[1, 2, 3]]), [[1, 2, 3]])

    def test_two_lists(self):
        self.assertEqual(merge([[1, 2, 3], [4, 5, 6]]), [[1, 4], [2, 5], [3, 6]])

    def test_three_lists(self):
        self.assertEqual(merge([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), [[1, 4, 7], [2, 5, 8], [3, 6, 9]])

    def test_lists_of_diff_lengths(self):
        self.assertEqual(merge([[1, 2, 3], [4, 5], [6, 7, 8, 9]]), [[1, 4, 6], [2, 5, 7], [3, 8], [8]])

    def test_lists_with_duplicates(self):
        self.assertEqual(merge([[1, 2, 2, 3], [4, 5, 5, 6]]), [[1, 4], [2, 5], [2, 5], [3, 6]])
