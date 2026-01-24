import unittest
from mbpp_4_code import heap_queue_largest

class TestHeapQueueLargest(unittest.TestCase):
    def test_typical_input(self):
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        n = 3
        self.assertEqual(heap_queue_largest(nums, n), [9, 8, 7])

    def test_edge_case_n_greater_than_length(self):
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        n = 11
        self.assertEqual(heap_queue_largest(nums, n), [10, 9, 8, 7, 6, 5, 4, 3, 2, 1])

    def test_edge_case_n_equal_to_length(self):
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        n = 10
        self.assertEqual(heap_queue_largest(nums, n), [10, 9, 8, 7, 6, 5, 4, 3, 2, 1])

    def test_edge_case_n_less_than_one(self):
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        n = 0
        self.assertEqual(heap_queue_largest(nums, n), [])

    def test_edge_case_empty_list(self):
        nums = []
        n = 3
        self.assertEqual(heap_queue_largest(nums, n), [])

    def test_edge_case_single_element_list(self):
        nums = [1]
        n = 1
        self.assertEqual(heap_queue_largest(nums, n), [1])

    def test_edge_case_single_element_list_n_greater_than_one(self):
        nums = [1]
        n = 2
        self.assertEqual(heap_queue_largest(nums, n), [1])

    def test_edge_case_invalid_input_type(self):
        nums = "abc"
        n = 3
        with self.assertRaises(TypeError):
            heap_queue_largest(nums, n)

    def test_edge_case_invalid_input_type_n(self):
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        n = "abc"
        with self.assertRaises(TypeError):
            heap_queue_largest(nums, n)
