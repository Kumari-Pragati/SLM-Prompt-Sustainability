import unittest
from mbpp_152_code import merge_sort

class TestMergeSort(unittest.TestCase):

    # Test for simple / typical inputs
    def test_typical_input(self):
        self.assertEqual(merge_sort([3, 1, 4, 1, 5, 9, 2, 6, 5, 3]), [1, 1, 2, 3, 3, 4, 5, 5, 6, 9])

    # Test for edge condition: empty input
    def test_empty_input(self):
        self.assertEqual(merge_sort([]), [])

    # Test for edge condition: single element input
    def test_single_element_input(self):
        self.assertEqual(merge_sort([5]), [5])

    # Test for edge condition: already sorted input
    def test_already_sorted_input(self):
        self.assertEqual(merge_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    # Test for edge condition: reverse sorted input
    def test_reverse_sorted_input(self):
        self.assertEqual(merge_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    # Test for edge condition: duplicate elements
    def test_duplicate_elements(self):
        self.assertEqual(merge_sort([3, 1, 4, 1, 5, 9, 2, 6, 5, 3]), [1, 1, 2, 3, 3, 4, 5, 5, 6, 9])

    # Test for complex scenario: input with negative numbers
    def test_negative_numbers(self):
        self.assertEqual(merge_sort([-5, -2, -8, -1, -3]), [-8, -5, -3, -2, -1])
