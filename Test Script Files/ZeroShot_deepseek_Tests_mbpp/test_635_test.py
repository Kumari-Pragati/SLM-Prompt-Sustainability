import unittest
from mbpp_635_code import heap_sort

class TestHeapSort(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(heap_sort([]), [])

    def test_single_element(self):
        self.assertEqual(heap_sort([1]), [1])

    def test_sorted_list(self):
        self.assertEqual(heap_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_reverse_sorted_list(self):
        self.assertEqual(heap_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_random_list(self):
        self.assertEqual(heap_sort([3, 1, 4, 1, 5, 9, 2, 6, 5, 3]), [1, 1, 2, 3, 3, 4, 5, 5, 6, 9])
