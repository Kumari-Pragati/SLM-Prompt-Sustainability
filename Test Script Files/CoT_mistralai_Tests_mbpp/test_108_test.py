import unittest
from mbpp_108_code import merge_sorted_list

class TestMergeSortedList(unittest.TestCase):
    def test_empty_lists(self):
        self.assertListEqual(merge_sorted_list([]), [])
        self.assertListEqual(merge_sorted_list([], [1]), [1])
        self.assertListEqual(merge_sorted_list([1], []), [1])

    def test_single_list(self):
        self.assertListEqual(merge_sorted_list([1]), [1])
        self.assertListEqual(merge_sorted_list([2]), [2])
        self.assertListEqual(merge_sorted_list([3]), [3])

    def test_two_lists(self):
        self.assertListEqual(merge_sorted_list([1, 2], [3, 4]), [1, 2, 3, 4])
        self.assertListEqual(merge_sorted_list([2, 3], [1]), [1, 2, 3])
        self.assertListEqual(merge_sorted_list([4, 5], [1, 2]), [1, 2, 4, 5])

    def test_three_lists(self):
        self.assertListEqual(merge_sorted_list([1, 2], [3, 4], [5, 6]), [1, 2, 3, 4, 5, 6])
        self.assertListEqual(merge_sorted_list([2, 3], [1], [5, 6]), [1, 2, 3, 5, 6])
        self.assertListEqual(merge_sorted_list([4, 5], [1, 2], [3]), [1, 2, 3, 4, 5])

    def test_duplicates(self):
        self.assertListEqual(merge_sorted_list([1, 1, 2], [2, 3]), [1, 1, 2, 2, 3])
        self.assertListEqual(merge_sorted_list([2, 2, 3], [1]), [1, 2, 2, 3])
        self.assertListEqual(merge_sorted_list([3, 4, 4], [1, 2]), [1, 2, 3, 4, 4])

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, merge_sorted_list, 1, 2, 3)
        self.assertRaises(TypeError, merge_sorted_list, [1], 2, 3)
        self.assertRaises(TypeError, merge_sorted_list, [1], [2], 3)
