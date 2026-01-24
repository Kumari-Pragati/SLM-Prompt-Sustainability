import unittest
from mbpp_940_code import heap_sort, heapify, shift_down

class TestHeapSort(unittest.TestCase):

    def test_heap_sort(self):
        self.assertEqual(heap_sort([5, 3, 2, 1, 6, 4]), [1, 2, 3, 4, 5, 6])
        self.assertEqual(heap_sort([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        self.assertEqual(heap_sort([1]), [1])
        self.assertEqual(heap_sort([]), [])

    def test_heapify(self):
        arr = [5, 3, 2, 1, 6, 4]
        heapify(arr)
        self.assertTrue(all(arr[i] >= arr[2 * i + 1] for i in range(len(arr) // 2)))
        self.assertTrue(all(arr[i] >= arr[2 * i + 2] for i in range(len(arr) // 2)))

    def test_shift_down(self):
        arr = [5, 3, 2, 1, 6, 4]
        shift_down(arr, 0, len(arr) - 1)
        self.assertTrue(all(arr[i] >= arr[2 * i + 1] for i in range(len(arr) // 2)))
        self.assertTrue(all(arr[i] >= arr[2 * i + 2] for i in range(len(arr) // 2)))
