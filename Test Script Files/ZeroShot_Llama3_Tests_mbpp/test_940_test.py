import unittest
from mbpp_940_code import shift_down, heapify

class TestHeapSort(unittest.TestCase):

    def test_heap_sort_empty_array(self):
        self.assertEqual(heap_sort([]), [])

    def test_heap_sort_single_element_array(self):
        self.assertEqual(heap_sort([5]), [5])

    def test_heap_sort_sorted_array(self):
        self.assertEqual(heap_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_heap_sort_unsorted_array(self):
        self.assertEqual(heap_sort([5, 3, 8, 6, 2, 7, 1, 4]), [1, 2, 3, 4, 5, 6, 7, 8])

    def test_heap_sort_negative_numbers(self):
        self.assertEqual(heap_sort([-5, -3, -8, -6, -2, -7, -1, -4]), [-8, -7, -6, -5, -4, -3, -2, -1])

    def test_heap_sort_duplicates(self):
        self.assertEqual(heap_sort([5, 3, 8, 6, 2, 7, 1, 4, 5, 3, 8, 6, 2, 7, 1, 4]), [1, 2, 3, 3, 4, 4, 5, 5, 6, 7, 7, 8, 8])
