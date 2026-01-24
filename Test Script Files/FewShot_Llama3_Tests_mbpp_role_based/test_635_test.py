import unittest
from mbpp_635_code import heap_sort

class TestHeapSort(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(heap_sort([]), [])

    def test_single_element_list(self):
        self.assertEqual(heap_sort([5]), [5])

    def test_sorted_list(self):
        self.assertEqual(heap_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_unsorted_list(self):
        self.assertEqual(heap_sort([5, 2, 8, 1, 3]), [1, 2, 3, 5, 8])

    def test_list_with_duplicates(self):
        self.assertEqual(heap_sort([1, 2, 2, 3, 3, 3, 4, 5]), [1, 2, 2, 3, 3, 3, 4, 5])

    def test_list_with_negative_numbers(self):
        self.assertEqual(heap_sort([-5, -2, 0, 1, 3]), [-5, -2, 0, 1, 3])
