import unittest
from mbpp_496_code import heap_queue_smallest

class TestHeapQueueSmallest(unittest.TestCase):

    def test_typical_input(self):
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        n = 3
        expected = [1, 2, 3]
        self.assertEqual(heap_queue_smallest(nums, n), expected)

    def test_edge_case_n_greater_than_length(self):
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        n = 11
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertEqual(heap_queue_smallest(nums, n), expected)

    def test_edge_case_n_equal_to_length(self):
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        n = 10
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertEqual(heap_queue_smallest(nums, n), expected)

    def test_edge_case_n_equal_to_zero(self):
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        n = 0
        expected = []
        self.assertEqual(heap_queue_smallest(nums, n), expected)

    def test_invalid_input_non_integer_n(self):
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        n = 'a'
        with self.assertRaises(TypeError):
            heap_queue_smallest(nums, n)

    def test_invalid_input_non_list_nums(self):
        nums = 'hello'
        n = 3
        with self.assertRaises(TypeError):
            heap_queue_smallest(nums, n)
