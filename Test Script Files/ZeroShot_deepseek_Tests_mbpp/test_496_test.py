import unittest
from mbpp_496_code import heap_queue_smallest

class TestHeapQueueSmallest(unittest.TestCase):

    def test_heap_queue_smallest(self):
        self.assertEqual(heap_queue_smallest([3, 1, 2, 5, 4], 3), [1, 2, 3])
        self.assertEqual(heap_queue_smallest([10, 20, 30, 40, 50], 2), [10, 20])
        self.assertEqual(heap_queue_smallest([1, 1, 1, 1, 1], 5), [1, 1, 1, 1, 1])
        self.assertEqual(heap_queue_smallest([], 0), [])
        self.assertEqual(heap_queue_smallest([10, 20, 30, 40, 50], 6), [10, 20, 30, 40, 50])
        self.assertEqual(heap_queue_smallest([1, 2, 3, 4, 5], 1), [1])
