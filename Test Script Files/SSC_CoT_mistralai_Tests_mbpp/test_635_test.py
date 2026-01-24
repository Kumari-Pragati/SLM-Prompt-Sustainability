import unittest
from mbpp_635_code import heap_sort

class TestHeapSort(unittest.TestCase):

    def test_heap_sort_normal(self):
        self.assertEqual(heap_sort([1, 5, 3, 9, 2]), [1, 3, 5, 9, 2])
        self.assertEqual(heap_sort([-1, -5, -3, -9, -2]), [-9, -5, -3, -2, -1])
        self.assertEqual(heap_sort([0]), [0])
        self.assertEqual(heap_sort([5, 3, 1]), [1, 3, 5])

    def test_heap_sort_edge_cases(self):
        self.assertEqual(heap_sort([]), [])
        self.assertEqual(heap_sort([1]), [1])
        self.assertEqual(heap_sort([1, 1]), [1, 1])
        self.assertEqual(heap_sort([1, 1, 1]), [1, 1, 1])
        self.assertEqual(heap_sort([float('inf'), 1]), [1, float('inf')])
        self.assertEqual(heap_sort([-float('inf'), -1]), [-1, -float('inf')])

    def test_heap_sort_invalid_inputs(self):
        with self.assertRaises(TypeError):
            heap_sort('string')
        with self.assertRaises(TypeError):
            heap_sort(1.5)
