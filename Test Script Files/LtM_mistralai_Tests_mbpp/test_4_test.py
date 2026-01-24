import unittest
from mbpp_4_code import heap_queue_largest

class TestHeapQueueLargest(unittest.TestCase):

    def test_simple(self):
        self.assertListEqual(heap_queue_largest([1, 2, 3, 4, 5], 2), [4, 5])
        self.assertListEqual(heap_queue_largest([10, 20, 30, 40, 50], 3), [50, 40, 30])

    def test_edge_cases(self):
        self.assertListEqual(heap_queue_largest([], 1), [])
        self.assertListEqual(heap_queue_largest([1], 1), [1])
        self.assertListEqual(heap_queue_largest([1, 2], 2), [2, 1])
        self.assertListEqual(heap_queue_largest([1, 2, 3], 4), [3, 2, 1])
        self.assertListEqual(heap_queue_largest([1, 2, 3], 5), [1, 2, 3])

    def test_complex(self):
        self.assertListEqual(heap_queue_largest([-10, -5, 0, 5, 10], 3), [10, 5, -5])
        self.assertListEqual(heap_queue_largest([-10, -5, 0, 5, 10], 4), [10, 5, -5, -10])
        self.assertListEqual(heap_queue_largest([-10, -5, 0, 5, 10], 5), [-10, -5, 0, 5, 10])
        self.assertListEqual(heap_queue_largest([-10, -5, 0, 5, 10], 6), [-10, -5, 0, 5, 10, -10])
