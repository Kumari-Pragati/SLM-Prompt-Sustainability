import unittest
from mbpp_635_code import heap_sort

class TestHeapSort(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(heap_sort([3, 2, 1, 4, 5]), [1, 2, 3, 4, 5])

    def test_empty_input(self):
        self.assertEqual(heap_sort([]), [])

    def test_single_element_input(self):
        self.assertEqual(heap_sort([5]), [5])

    def test_duplicate_elements(self):
        self.assertEqual(heap_sort([3, 1, 2, 2, 3]), [1, 2, 2, 3, 3])

    def test_negative_numbers(self):
        self.assertEqual(heap_sort([-3, -1, -2, -4, -5]), [-5, -4, -3, -2, -1])

    def test_mixed_numbers(self):
        self.assertEqual(heap_sort([3, -1, 2, -2, 1]), [-2, -1, 1, 2, 3])
