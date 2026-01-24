import unittest
from mbpp_496_code import heap_queue_smallest

class TestHeapQueueSmallest(unittest.TestCase):

    def test_heap_queue_smallest(self):
        nums = [4, 2, 9, 6, 23, 12, 34, 1]
        n = 3
        expected = [1, 2, 4]
        self.assertEqual(heap_queue_smallest(nums, n), expected)

        nums = [1, 2, 3, 4, 5, 6]
        n = 2
        expected = [1, 2]
        self.assertEqual(heap_queue_smallest(nums, n), expected)

        nums = [5, 4, 3, 2, 1]
        n = 3
        expected = [1, 2, 3]
        self.assertEqual(heap_queue_smallest(nums, n), expected)

        nums = []
        n = 0
        expected = []
        self.assertEqual(heap_queue_smallest(nums, n), expected)

        nums = [1]
        n = 1
        expected = [1]
        self.assertEqual(heap_queue_smallest(nums, n), expected)
