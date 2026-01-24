import unittest
from mbpp_4_code import heap_queue_largest

class TestHeapQueueLargest(unittest.TestCase):

    def test_typical_case(self):
        nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
        n = 4
        result = heap_queue_largest(nums, n)
        self.assertEqual(result, [9, 6, 5, 5])

    def test_empty_list(self):
        nums = []
        n = 3
        result = heap_queue_largest(nums, n)
        self.assertEqual(result, [])

    def test_single_element(self):
        nums = [7]
        n = 1
        result = heap_queue_largest(nums, n)
        self.assertEqual(result, [7])

    def test_large_n(self):
        nums = [1, 2, 3, 4, 5]
        n = 10
        result = heap_queue_largest(nums, n)
        self.assertEqual(result, [5, 4, 3, 2, 1])

    def test_n_greater_than_list_length(self):
        nums = [1, 2, 3]
        n = 5
        result = heap_queue_largest(nums, n)
        self.assertEqual(result, [3, 2, 1])

    def test_negative_numbers(self):
        nums = [-3, -1, -4, -1, -5, -9, -2, -6, -5, -3, -5]
        n = 4
        result = heap_queue_largest(nums, n)
        self.assertEqual(result, [-1, -2, -3, -5])

    def test_duplicate_numbers(self):
        nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
        n = 4
        result = heap_queue_largest(nums, n)
        self.assertEqual(result, [9, 6, 5, 5])
