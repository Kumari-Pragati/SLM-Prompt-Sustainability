import unittest
from mbpp_635_code import heap_sort

class TestHeapSort(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(heap_sort([3, 1, 2]), [1, 2, 3])

    def test_empty_list(self):
        self.assertEqual(heap_sort([]), [])

    def test_single_element(self):
        self.assertEqual(heap_sort([5]), [5])

    def test_duplicate_elements(self):
        self.assertEqual(heap_sort([3, 1, 2, 2, 3]), [1, 2, 2, 3, 3])

    def test_negative_numbers(self):
        self.assertEqual(heap_sort([-3, -1, -2]), [-3, -2, -1])

    def test_large_numbers(self):
        self.assertEqual(heap_sort([100, 50, 150, 10, 20]), [10, 20, 50, 100, 150])

    def test_mixed_numbers(self):
        self.assertEqual(heap_sort([10, 5, 20, 15]), [5, 10, 15, 20])
