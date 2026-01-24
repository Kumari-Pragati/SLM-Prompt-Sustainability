import unittest
from mbpp_4_code import heap_queue_largest

class TestHeapQueueLargest(unittest.TestCase):

    def test_heap_queue_largest(self):
        self.assertEqual(heap_queue_largest([1, 2, 3, 4, 5], 3), [5, 4, 3])
        self.assertEqual(heap_queue_largest([5, 2, 8, 12, 3], 2), [12, 8])
        self.assertEqual(heap_queue_largest([1, 2, 3, 4, 5], 5), [5, 4, 3, 2, 1])
        self.assertEqual(heap_queue_largest([1, 2, 3, 4, 5], 0), [])
        self.assertEqual(heap_queue_largest([1, 2, 3, 4, 5], 6), [5, 4, 3, 2, 1])
