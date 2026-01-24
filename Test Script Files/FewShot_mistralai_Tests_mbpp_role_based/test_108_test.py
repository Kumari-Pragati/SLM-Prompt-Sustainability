import unittest
from mbpp_108_code import merge_sorted_list

class TestMergeSortedList(unittest.TestCase):
    def test_merge_three_empty_lists(self):
        self.assertEqual(merge_sorted_list([]), [])

    def test_merge_one_element_lists(self):
        self.assertEqual(merge_sorted_list([1]), [1])
        self.assertEqual(merge_sorted_list([2]), [2])
        self.assertEqual(merge_sorted_list([3]), [3])

    def test_merge_two_lists(self):
        self.assertEqual(merge_sorted_list([1, 2], [3, 4]), [1, 2, 3, 4])
        self.assertEqual(merge_sorted_list([4, 3], [2, 1]), [1, 2, 3, 4])

    def test_merge_three_lists(self):
        self.assertEqual(merge_sorted_list([1, 2], [3, 4], [5, 6]), [1, 2, 3, 4, 5, 6])
        self.assertEqual(merge_sorted_list([5, 6], [1, 2], [3, 4]), [1, 2, 3, 4, 5, 6])
        self.assertEqual(merge_sorted_list([3, 4], [1, 2], [5, 6]), [1, 2, 3, 4, 5, 6])

    def test_merge_lists_with_duplicates(self):
        self.assertEqual(merge_sorted_list([1, 1, 2], [2, 3], [3, 3]), [1, 1, 2, 2, 3, 3])
        self.assertEqual(merge_sorted_list([3, 3], [1, 1, 2], [2, 3]), [1, 1, 2, 2, 3, 3])
        self.assertEqual(merge_sorted_list([2, 3], [1, 1, 2], [3, 3]), [1, 1, 2, 2, 3, 3])
