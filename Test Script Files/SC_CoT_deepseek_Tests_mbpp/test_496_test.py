import unittest
from mbpp_496_code import heap_queue_smallest

class TestHeapQueueSmallest(unittest.TestCase):

    def test_typical_case(self):
        nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
        n = 4
        self.assertEqual(heap_queue_smallest(nums, n), [1, 1, 2, 3])

    def test_edge_case_n_equals_zero(self):
        nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
        n = 0
        self.assertEqual(heap_queue_smallest(nums, n), [])

    def test_edge_case_n_equals_length_of_nums(self):
        nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
        n = len(nums)
        self.assertEqual(heap_queue_smallest(nums, n), sorted(nums))

    def test_corner_case_repeated_smallest_numbers(self):
        nums = [3, 1, 1, 1, 5, 9, 2, 6, 5, 3, 5]
        n = 3
        self.assertEqual(heap_queue_smallest(nums, n), [1, 1, 1])

    def test_invalid_input_n_greater_than_length_of_nums(self):
        nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
        n = 20
        with self.assertRaises(ValueError):
            heap_queue_smallest(nums, n)

    def test_invalid_input_n_is_negative(self):
        nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
        n = -2
        with self.assertRaises(ValueError):
            heap_queue_smallest(nums, n)
