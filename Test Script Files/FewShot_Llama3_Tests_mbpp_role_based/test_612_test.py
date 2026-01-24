import unittest
from mbpp_612_code import merge

class TestMerge(unittest.TestCase):
    def test_merge_single_list(self):
        lst = [[1, 2, 3], [4, 5, 6]]
        expected = [[1, 4], [2, 5], [3, 6]]
        self.assertEqual(merge(lst), expected)

    def test_merge_multiple_lists(self):
        lst = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        expected = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
        self.assertEqual(merge(lst), expected)

    def test_merge_empty_list(self):
        lst = []
        expected = []
        self.assertEqual(merge(lst), expected)

    def test_merge_list_with_single_element(self):
        lst = [[1]]
        expected = [[1]]
        self.assertEqual(merge(lst), expected)

    def test_merge_list_with_empty_sublist(self):
        lst = [[1, 2, 3], [], [4, 5, 6]]
        expected = [[1, 4], [2, 5], [3, 6]]
        self.assertEqual(merge(lst), expected)
