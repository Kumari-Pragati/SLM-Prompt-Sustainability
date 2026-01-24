import unittest
from mbpp_4_code import heap_queue_largest

class TestHeapQueueLargest(unittest.TestCase):

    def test_heap_queue_largest(self):
        self.assertEqual(heap_queue_largest([1, 2, 3, 4, 5], 3), [5, 4, 3])
        self.assertEqual(heap_queue_largest([10, 20, 30, 40, 50], 2), [50, 40])
        self.assertEqual(heap_queue_largest([1, 1, 1, 1, 1], 5), [1, 1, 1, 1, 1])
        self.assertEqual(heap_queue_largest([], 0), [])
        self.assertEqual(heap_queue_largest([1, 2, 3, 4, 5], 1), [5])
        self.assertEqual(heap_queue_largest([1, 2, 3, 4, 5], 6), [5, 4, 3, 2, 1])
