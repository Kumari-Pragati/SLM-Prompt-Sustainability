import unittest
from mbpp_943_code import combine_lists

class TestCombineLists(unittest.TestCase):

    def test_combine_empty_lists(self):
        self.assertListEqual(combine_lists([]), [])
        self.assertListEqual(combine_lists([], [1]), [1])
        self.assertListEqual(combine_lists([], [1, 2]), [1, 2])

    def test_combine_single_element_lists(self):
        self.assertListEqual(combine_lists([1], []), [1])
        self.assertListEqual(combine_lists([], [1]), [1])
        self.assertListEqual(combine_lists([1], [2]), [1, 2])
        self.assertListEqual(combine_lists([2], [1]), [1, 2])

    def test_combine_equal_length_lists(self):
        self.assertListEqual(combine_lists([1, 2], [3, 4]), [1, 2, 3, 4])
        self.assertListEqual(combine_lists([3, 4], [1, 2]), [1, 2, 3, 4])
        self.assertListEqual(combine_lists([1, 2, 3], [4, 5, 6]), [1, 2, 3, 4, 5, 6])
        self.assertListEqual(combine_lists([4, 5, 6], [1, 2, 3]), [1, 2, 3, 4, 5, 6])

    def test_combine_unequal_length_lists(self):
        self.assertListEqual(combine_lists([1, 2], [3]), [1, 2, 3])
        self.assertListEqual(combine_lists([3], [1, 2]), [1, 2, 3])
        self.assertListEqual(combine_lists([1, 2, 3], [4, 5]), [1, 2, 3, 4, 5])
        self.assertListEqual(combine_lists([4, 5], [1, 2, 3]), [1, 2, 3, 4, 5])

    def test_combine_lists_with_duplicates(self):
        self.assertListEqual(combine_lists([1, 1, 2], [2, 2, 3]), [1, 1, 2, 2, 2, 3])
        self.assertListEqual(combine_lists([2, 2, 3], [1, 1, 2]), [1, 1, 2, 2, 2, 3])
        self.assertListEqual(combine_lists([1, 2, 3, 3], [4, 5, 6]), [1, 2, 3, 3, 4, 5, 6])
        self.assertListEqual(combine_lists([4, 5, 6], [1, 2, 3, 3]), [1, 2, 3, 3, 4, 5, 6])

    def test_combine_lists_with_negative_numbers(self):
        self.assertListEqual(combine_lists([-1, 0, 1], [-2, -3, 4]), [-1, -2, -3, 0, 1, 4])
        self.assertListEqual(combine_lists([-2, -3, 4], [-1, 0, 1]), [-1, -2, -3, 0, 1, 4])
        self.assertListEqual(combine_lists([-1, 0, 1, -1], [-2, -3, 4, -2]), [-1, -1, -2, -2, -3, 0, 1, 4])
        self.assertListEqual(combine_lists([-2, -3, 4, -2], [-1, 0, 1, -1]), [-1, -1, -2, -2, -3, 0, 1, 4])