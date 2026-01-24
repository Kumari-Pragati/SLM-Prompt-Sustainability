import unittest
from mbpp_108_code import merge_sorted_list

class TestMergeSortedList(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(merge_sorted_list([1, 3, 5], [2, 4, 6], [0, 7, 8]), [0, 1, 2, 3, 4, 5, 6, 7, 8])

    def test_empty_lists(self):
        self.assertEqual(merge_sorted_list([], [], []), [])

    def test_single_element_lists(self):
        self.assertEqual(merge_sorted_list([1], [2], [3]), [1, 2, 3])

    def test_duplicate_elements(self):
        self.assertEqual(merge_sorted_list([1, 2, 2], [2, 3, 4], [2, 4, 5]), [1, 2, 2, 2, 2, 3, 4, 4, 5])

    def test_negative_numbers(self):
        self.assertEqual(merge_sorted_list([-1, -3, -5], [-2, -4, -6], [-7, -8, -10]), [-10, -8, -7, -6, -5, -4, -3, -2, -1])

    def test_large_numbers(self):
        self.assertEqual(merge_sorted_list([1000, 2000, 3000], [1500, 2500, 3500], [2000, 3000, 4000]), [1000, 1500, 2000, 2000, 2500, 3000, 3000, 3500, 4000])
