import unittest
from mbpp_4_code import heap_queue_largest

class TestHeapQueueLargest(unittest.TestCase):
    def test_typical_use_case(self):
        nums = [1, 8, 2, 23, 7, -4, 18, 0, 15, 20]
        n = 5
        self.assertEqual(heap_queue_largest(nums, n), [23, 20, 18, 15, 8])

    def test_edge_case_with_empty_list(self):
        nums = []
        n = 5
        self.assertEqual(heap_queue_largest(nums, n), [])

    def test_boundary_case_with_n_greater_than_length_of_nums(self):
        nums = [1, 8, 2, 23, 7, -4, 18, 0, 15, 20]
        n = 20
        self.assertEqual(heap_queue_largest(nums, n), nums)

    def test_error_handling_with_invalid_input(self):
        nums = [1, 8, 2, 23, 7, -4, 18, 0, 15, 20]
        n = 'five'
        with self.assertRaises(TypeError):
            heap_queue_largest(nums, n)
