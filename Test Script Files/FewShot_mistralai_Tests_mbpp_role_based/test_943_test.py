import unittest
from mbpp_943_code import combine_lists

class TestCombineLists(unittest.TestCase):
    def test_combine_empty_lists(self):
        self.assertEqual(combine_lists([]), [])

    def test_combine_single_element_lists(self):
        self.assertEqual(combine_lists([1]), [1])
        self.assertEqual(combine_lists([2]), [2])

    def test_combine_lists_with_duplicates(self):
        self.assertEqual(combine_lists([1, 1, 2]), [1, 1, 2])
        self.assertEqual(combine_lists([2, 2, 1]), [1, 2, 2])

    def test_combine_lists_with_different_lengths(self):
        self.assertEqual(combine_lists([1, 2], [3, 4]), [1, 2, 3, 4])
        self.assertEqual(combine_lists([3, 4], [1, 2]), [1, 2, 3, 4])

    def test_combine_lists_with_negative_numbers(self):
        self.assertEqual(combine_lists([1, -2, 3], [-4, -5, 6]), [1, -2, 3, -4, -5, 6])
        self.assertEqual(combine_lists([-1, -2, -3], [4, 5, 6]), [4, 5, 6, -1, -2, -3])
