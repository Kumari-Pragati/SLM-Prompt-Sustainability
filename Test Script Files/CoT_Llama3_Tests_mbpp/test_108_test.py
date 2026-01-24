import unittest
from mbpp_108_code import merge_sorted_list

class TestMergeSortedList(unittest.TestCase):
    def test_empty_lists(self):
        self.assertEqual(merge_sorted_list([], [], []), [])

    def test_single_list(self):
        self.assertEqual(merge_sorted_list([1, 2, 3], [], []), [1, 2, 3])

    def test_two_lists(self):
        self.assertEqual(merge_sorted_list([1, 2, 3], [4, 5, 6], []), [1, 2, 3, 4, 5, 6])

    def test_three_lists(self):
        self.assertEqual(merge_sorted_list([1, 2, 3], [4, 5, 6], [7, 8, 9]), [1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_duplicates(self):
        self.assertEqual(merge_sorted_list([1, 2, 2, 3], [2, 3, 4], [3, 4, 5]), [1, 2, 2, 3, 3, 4, 5])

    def test_negative_numbers(self):
        self.assertEqual(merge_sorted_list([-1, -2, -3], [1, 2, 3], [4, 5, 6]), [-3, -2, -1, 1, 2, 3, 4, 5, 6])
