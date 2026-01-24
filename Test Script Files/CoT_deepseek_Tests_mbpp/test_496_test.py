import unittest
from mbpp_496_code import heap_queue_smallest

class TestHeapQueueSmallest(unittest.TestCase):

    def test_typical_case(self):
        nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
        n = 4
        expected_output = [1, 1, 2, 3]
        self.assertEqual(heap_queue_smallest(nums, n), expected_output)

    def test_empty_list(self):
        nums = []
        n = 5
        expected_output = []
        self.assertEqual(heap_queue_smallest(nums, n), expected_output)

    def test_large_n(self):
        nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
        n = 15
        expected_output = [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]
        self.assertEqual(heap_queue_smallest(nums, n), expected_output)

    def test_n_equals_zero(self):
        nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
        n = 0
        expected_output = []
        self.assertEqual(heap_queue_smallest(nums, n), expected_output)

    def test_negative_numbers(self):
        nums = [-3, -1, -4, -1, -5, -9, -2, -6, -5, -3, -5]
        n = 4
        expected_output = [-9, -6, -5, -5]
        self.assertEqual(heap_queue_smallest(nums, n), expected_output)
