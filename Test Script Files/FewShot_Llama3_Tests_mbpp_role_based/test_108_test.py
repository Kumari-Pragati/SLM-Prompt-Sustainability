import unittest
from mbpp_108_code import merge_sorted_list

class TestMergeSortedList(unittest.TestCase):
    def test_empty_lists(self):
        self.assertEqual(merge_sorted_list([], [], []), [])

    def test_single_list(self):
        self.assertEqual(merge_sorted_list([1, 2, 3], [], []), [1, 2, 3])

    def test_two_lists(self):
        self.assertEqual(merge_sorted_list([1, 3, 5], [2, 4, 6], []), [1, 2, 3, 4, 5, 6])

    def test_three_lists(self):
        self.assertEqual(merge_sorted_list([1, 3, 5], [2, 4, 6], [0, 7, 8]), [0, 1, 2, 3, 4, 5, 6, 7, 8])

    def test_negative_numbers(self):
        self.assertEqual(merge_sorted_list([-1, -3, -5], [-2, -4, -6], []), [-6, -5, -4, -3, -2, -1])

    def test_duplicates(self):
        self.assertEqual(merge_sorted_list([1, 2, 2, 3, 3, 3], [2, 4, 4], [3, 5, 5]), [1, 2, 2, 3, 3, 4, 5, 5])
