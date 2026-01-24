import unittest
from mbpp_943_code import combine_lists

class TestCombineLists(unittest.TestCase):

    def test_empty_lists(self):
        self.assertEqual(combine_lists([], []), [])

    def test_single_list(self):
        self.assertEqual(combine_lists([1, 2, 3], []), [1, 2, 3])
        self.assertEqual(combine_lists([], [4, 5, 6]), [4, 5, 6])

    def test_sorted_lists(self):
        self.assertEqual(combine_lists([1, 2, 3], [4, 5, 6]), [1, 2, 3, 4, 5, 6])
        self.assertEqual(combine_lists([1, 2, 3, 4, 5], [6, 7, 8, 9, 10]), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    def test_unsorted_lists(self):
        self.assertEqual(combine_lists([3, 1, 2], [4, 5, 6]), [1, 2, 3, 4, 5, 6])
        self.assertEqual(combine_lists([5, 4, 3], [2, 1, 6]), [1, 2, 3, 4, 5, 6])

    def test_duplicates(self):
        self.assertEqual(combine_lists([1, 2, 2, 3], [2, 3, 4, 5]), [1, 2, 2, 3, 4, 5])
