import unittest
from mbpp_4_code import heap_queue_largest

class TestHeapQueueLargest(unittest.TestCase):
    def test_typical_use_case(self):
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        n = 3
        expected_result = [9, 8, 7]
        self.assertEqual(heap_queue_largest(nums, n), expected_result)

    def test_edge_case_n_zero(self):
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        n = 0
        expected_result = []
        self.assertEqual(heap_queue_largest(nums, n), expected_result)

    def test_edge_case_n_equal_to_length(self):
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        n = 10
        expected_result = sorted(nums, reverse=True)
        self.assertEqual(heap_queue_largest(nums, n), expected_result)

    def test_invalid_input_type(self):
        nums = "hello"
        n = 3
        with self.assertRaises(TypeError):
            heap_queue_largest(nums, n)
