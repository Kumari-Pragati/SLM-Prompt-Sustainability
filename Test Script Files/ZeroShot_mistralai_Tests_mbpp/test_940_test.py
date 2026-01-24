import unittest
from mbpp_940_code import heap_sort, heapify, shift_down

class TestHeapSort(unittest.TestCase):

    def test_heap_sort_empty_list(self):
        self.assertEqual(heap_sort([]), [])

    def test_heap_sort_single_element(self):
        self.assertEqual(heap_sort([5]), [5])

    def test_heap_sort_simple_list(self):
        self.assertEqual(heap_sort([5, 3, 1, 4, 2]), [2, 3, 4, 5, 1])

    def test_heap_sort_reverse_list(self):
        self.assertEqual(heap_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_heap_sort_duplicates(self):
        self.assertEqual(heap_sort([5, 5, 3, 1, 4, 4, 2]), [2, 3, 4, 4, 5, 5, 1])

    def test_heapify_empty_list(self):
        self.assertEqual(heapify([]), None)

    def test_heapify_single_element(self):
        arr = [5]
        heapify(arr)
        self.assertEqual(arr, [5])

    def test_heapify_simple_list(self):
        arr = [5, 3, 1, 4, 2]
        heapify(arr)
        self.assertEqual(heap_sort(arr), [2, 3, 4, 5, 1])

    def test_heapify_reverse_list(self):
        arr = [5, 4, 3, 2, 1]
        heapify(arr)
        self.assertEqual(heap_sort(arr), [1, 2, 3, 4, 5])

    def test_heapify_duplicates(self):
        arr = [5, 5, 3, 1, 4, 4, 2]
        heapify(arr)
        self.assertEqual(heap_sort(arr), [2, 3, 4, 4, 5, 5, 1])

    def test_shift_down_empty_list(self):
        self.assertEqual(shift_down([], 0, 0), None)

    def test_shift_down_single_element(self):
        self.assertEqual(shift_down([5], 0, 0), None)

    def test_shift_down_simple_list(self):
        self.assertEqual(shift_down([5, 3, 1], 0, 2), [5, 3, 1])

    def test_shift_down_reverse_list(self):
        self.assertEqual(shift_down([5, 4, 3], 0, 2), [5, 4, 3])

    def test_shift_down_duplicates(self):
        self.assertEqual(shift_down([5, 5, 3], 0, 1), [5, 5, 3])
