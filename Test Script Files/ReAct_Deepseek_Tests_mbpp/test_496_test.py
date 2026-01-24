import unittest
from mbpp_496_code import heap_queue_smallest

class TestHeapQueueSmallest(unittest.TestCase):

    def test_typical_case(self):
        nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
        n = 4
        result = heap_queue_smallest(nums, n)
        self.assertEqual(result, [1, 1, 2, 3])

    def test_empty_list(self):
        nums = []
        n = 5
        result = heap_queue_smallest(nums, n)
        self.assertEqual(result, [])

    def test_large_n(self):
        nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
        n = 15
        result = heap_queue_smallest(nums, n)
        self.assertEqual(result, [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9])

    def test_small_n(self):
        nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
        n = 0
        result = heap_queue_smallest(nums, n)
        self.assertEqual(result, [])

    def test_negative_numbers(self):
        nums = [-3, -1, -4, -1, -5, -9, -2, -6, -5, -3, -5]
        n = 4
        result = heap_queue_smallest(nums, n)
        self.assertEqual(result, [-9, -6, -5, -5])

    def test_duplicate_numbers(self):
        nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
        n = 4
        result = heap_queue_smallest(nums, n)
        self.assertEqual(result, [1, 1, 2, 3])
