import unittest
from mbpp_496_code import heap_queue_smallest

class TestHeapQueueSmallest(unittest.TestCase):
    def test_typical_case(self):
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        n = 3
        expected = [1, 2, 3]
        self.assertEqual(heap_queue_smallest(nums, n), expected)

    def test_edge_case_n_zero(self):
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        n = 0
        self.assertEqual(heap_queue_smallest(nums, n), [])

    def test_edge_case_n_equal_to_length(self):
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        n = 10
        expected = nums
        self.assertEqual(heap_queue_smallest(nums, n), expected)

    def test_edge_case_empty_list(self):
        nums = []
        n = 3
        self.assertEqual(heap_queue_smallest(nums, n), [])

    def test_edge_case_n_greater_than_length(self):
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        n = 15
        self.assertEqual(heap_queue_smallest(nums, n), nums)
