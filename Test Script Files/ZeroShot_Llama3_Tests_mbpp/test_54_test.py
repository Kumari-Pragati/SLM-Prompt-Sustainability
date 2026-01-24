import unittest
from mbpp_54_code import counting_sort

class TestCountingSort(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(counting_sort([]), [])

    def test_single_element_list(self):
        self.assertEqual(counting_sort([1]), [1])

    def test_sorted_list(self):
        self.assertEqual(counting_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_unsorted_list(self):
        self.assertEqual(counting_sort([5, 1, 4, 2, 3]), [1, 2, 3, 4, 5])

    def test_duplicates(self):
        self.assertEqual(counting_sort([1, 2, 2, 3, 3, 3, 4, 5, 5]), [1, 2, 2, 3, 3, 3, 4, 5, 5])

    def test_negative_numbers(self):
        self.assertEqual(counting_sort([-5, -3, -1, 0, 1, 2, 3, 5]), [-5, -3, -1, 0, 1, 2, 3, 5])

    def test_large_list(self):
        self.assertEqual(counting_sort([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
