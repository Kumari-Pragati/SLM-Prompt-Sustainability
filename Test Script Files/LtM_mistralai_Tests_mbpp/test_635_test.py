import unittest
from mbpp_635_code import heap_sort

class TestHeapSort(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(heap_sort([1, 2, 3]), [1, 2, 3])
        self.assertEqual(heap_sort([3, 2, 1]), [1, 2, 3])
        self.assertEqual(heap_sort([-1, -2, -3]), [-3, -2, -1])

    def test_edge_cases(self):
        self.assertEqual(heap_sort([]), [])
        self.assertEqual(heap_sort([1]), [1])
        self.assertEqual(heap_sort([1000000000]), [1000000000])

    def test_complex(self):
        self.assertEqual(heap_sort([5, 3, 1, 4, 2]), [1, 2, 3, 4, 5])
        self.assertEqual(heap_sort([5, 3, 1, 4, 2, 0]), [0, 1, 2, 3, 4, 5])
        self.assertEqual(heap_sort([5, 3, 1, 4, 2, 0, -1]), [-1, 0, 1, 2, 3, 4, 5])
