import unittest
from mbpp_943_code import combine_lists

class TestCombineLists(unittest.TestCase):
    def test_empty_lists(self):
        self.assertEqual(combine_lists([], []), [])

    def test_single_list(self):
        self.assertEqual(combine_lists([1, 2, 3], []), [1, 2, 3])
        self.assertEqual(combine_lists([], [4, 5, 6]), [4, 5, 6])

    def test_merged_lists(self):
        self.assertEqual(combine_lists([1, 2, 3], [4, 5, 6]), [1, 2, 3, 4, 5, 6])

    def test_sorted_lists(self):
        self.assertEqual(combine_lists([1, 2, 3], [2, 3, 4]), [1, 2, 2, 3, 3, 4])
        self.assertEqual(combine_lists([1, 2, 3], [1, 2, 3]), [1, 1, 2, 2, 3, 3])

    def test_duplicates(self):
        self.assertEqual(combine_lists([1, 2, 2, 3], [2, 3, 3, 4]), [1, 2, 2, 2, 3, 3, 3, 4])
