import unittest
from mbpp_943_code import combine_lists

class TestCombineLists(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(combine_lists([1, 3, 5], [2, 4, 6]), [1, 2, 3, 4, 5, 6])

    def test_empty_lists(self):
        self.assertEqual(combine_lists([], []), [])

    def test_one_empty_list(self):
        self.assertEqual(combine_lists([1, 2, 3], []), [1, 2, 3])
        self.assertEqual(combine_lists([], [4, 5, 6]), [4, 5, 6])

    def test_duplicate_elements(self):
        self.assertEqual(combine_lists([1, 2, 2], [2, 3, 4]), [1, 2, 2, 2, 3, 4])

    def test_negative_numbers(self):
        self.assertEqual(combine_lists([-1, -3, -5], [-2, -4, -6]), [-6, -5, -4, -3, -2, -1])

    def test_sorted_lists(self):
        self.assertEqual(combine_lists([1, 3, 5], [2, 4, 6]), [1, 2, 3, 4, 5, 6])
        self.assertEqual(combine_lists([6, 4, 2], [5, 3, 1]), [1, 2, 3, 4, 5, 6])
