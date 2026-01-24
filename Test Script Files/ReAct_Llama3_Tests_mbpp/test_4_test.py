import unittest
from mbpp_4_code import heap_queue_largest

class TestHeapQueueLargest(unittest.TestCase):
    def test_typical_case(self):
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        n = 3
        expected = [9, 8, 7]
        self.assertEqual(heap_queue_largest(nums, n), expected)

    def test_edge_case_n_zero(self):
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        n = 0
        with self.assertRaises(ValueError):
            heap_queue_largest(nums, n)

    def test_edge_case_n_greater_than_length(self):
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        n = 15
        expected = sorted(nums, reverse=True)[:n]
        self.assertEqual(heap_queue_largest(nums, n), expected)

    def test_edge_case_empty_list(self):
        nums = []
        n = 3
        with self.assertRaises(IndexError):
            heap_queue_largest(nums, n)

    def test_edge_case_n_is_one(self):
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        n = 1
        expected = [10]
        self.assertEqual(heap_queue_largest(nums, n), expected)
