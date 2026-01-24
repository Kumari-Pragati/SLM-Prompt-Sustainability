import unittest
from mbpp_635_code import heap_sort

class TestHeapSort(unittest.TestCase):
    def test_empty_input(self):
        self.assertEqual(heap_sort([]), [])

    def test_single_element_input(self):
        self.assertEqual(heap_sort([1]), [1])

    def test_multiple_elements_input(self):
        self.assertEqual(heap_sort([5, 2, 8, 1, 3]), [1, 2, 3, 5, 8])

    def test_negative_numbers_input(self):
        self.assertEqual(heap_sort([-5, 2, -8, 1, 3]), [-8, -5, 1, 2, 3])

    def test_duplicates_input(self):
        self.assertEqual(heap_sort([5, 2, 8, 1, 3, 5, 2]), [1, 2, 2, 3, 5, 5, 8])

    def test_max_value_input(self):
        self.assertEqual(heap_sort([5, 2, 8, 1, 3, 100]), [1, 2, 3, 5, 8, 100])

    def test_min_value_input(self):
        self.assertEqual(heap_sort([-5, -8, -10, -1, -3]), [-10, -8, -5, -3, -1])
