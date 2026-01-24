import unittest
from540_code import find_Diff

class TestFindDiff(unittest.TestCase):

    def test_find_diff_empty_list(self):
        self.assertEqual(find_Diff([], 0), 0)

    def test_find_diff_single_element(self):
        self.assertEqual(find_Diff([1], 1), 0)

    def test_find_diff_duplicates(self):
        self.assertEqual(find_Diff([1, 1, 1], 3), 0)

    def test_find_diff_single_duplicate(self):
        self.assertEqual(find_Diff([1, 1, 2], 3), 1)

    def test_find_diff_multiple_duplicates(self):
        self.assertEqual(find_Diff([1, 1, 2, 2, 3], 5), 0)

    def test_find_diff_unsorted_list(self):
        self.assertEqual(find_Diff([3, 1, 1, 2, 2, 3], 6), 2)

    def test_find_diff_large_list(self):
        arr = [i for i in range(100)]
        self.assertEqual(find_Diff(arr, len(arr)), 0)
