import unittest
from mbpp_496_code import heap_queue_smallest

class TestHeapQueueSmallest(unittest.TestCase):
    def test_typical_use_case(self):
        nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
        n = 4
        self.assertEqual(heap_queue_smallest(nums, n), [1, 1, 2, 3])

    def test_edge_case_with_empty_list(self):
        nums = []
        n = 5
        self.assertEqual(heap_queue_smallest(nums, n), [])

    def test_boundary_case_with_large_n(self):
        nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
        n = 11
        self.assertEqual(heap_queue_smallest(nums, n), [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9])

    def test_boundary_case_with_small_n(self):
        nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
        n = 0
        self.assertEqual(heap_queue_smallest(nums, n), [])

    def test_error_handling_with_invalid_n(self):
        nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
        n = -1
        with self.assertRaises(ValueError):
            heap_queue_smallest(nums, n)
