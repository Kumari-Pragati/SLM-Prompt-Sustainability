import unittest
from mbpp_943_code import combine_lists

class TestCombineLists(unittest.TestCase):

    def test_combine_simple_lists(self):
        self.assertEqual(combine_lists([1, 2, 3], [4, 5, 6]), [1, 2, 3, 4, 5, 6])

    def test_combine_empty_lists(self):
        self.assertEqual(combine_lists([], []), [])

    def test_combine_one_empty_list(self):
        self.assertEqual(combine_lists([1, 2, 3], []), [1, 2, 3])
        self.assertEqual(combine_lists([], [4, 5, 6]), [4, 5, 6])

    def test_combine_sorted_lists(self):
        self.assertEqual(combine_lists([1, 3, 5], [2, 4, 6]), [1, 2, 3, 4, 5, 6])

    def test_combine_unsorted_lists(self):
        self.assertEqual(combine_lists([3, 1, 5], [2, 4, 6]), [1, 2, 3, 4, 5, 6])

    def test_combine_duplicate_elements(self):
        self.assertEqual(combine_lists([1, 2, 2], [2, 3, 4]), [1, 2, 2, 2, 3, 4])
