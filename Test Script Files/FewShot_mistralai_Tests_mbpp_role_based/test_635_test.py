import unittest
from mbpp_635_code import heap_sort

class TestHeapSort(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(heap_sort([]), [])

    def test_single_element_list(self):
        self.assertEqual(heap_sort([4]), [4])

    def test_positive_numbers(self):
        self.assertEqual(heap_sort([5, 3, 1, 4, 2]), [1, 2, 3, 4, 5])

    def test_negative_numbers(self):
        self.assertEqual(heap_sort([-5, -3, -1, -4, -2]), [-5, -4, -3, -2, -1])

    def test_mixed_numbers(self):
        self.assertEqual(heap_sort([5, -3, 1, 4, -2]), [1, -2, 3, 4, 5])

    def test_duplicates(self):
        self.assertEqual(heap_sort([5, 5, 3, 1, 4, 2]), [1, 2, 3, 4, 5, 5])
