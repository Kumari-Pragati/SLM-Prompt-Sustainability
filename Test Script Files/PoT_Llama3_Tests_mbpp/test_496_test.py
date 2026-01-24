import unittest
from mbpp_496_code import heap_queue_smallest

class TestHeapQueueSmallest(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(heap_queue_smallest([1, 2, 3, 4, 5], 3), [1, 2, 3])

    def test_edge_case_n_zero(self):
        self.assertEqual(heap_queue_smallest([1, 2, 3, 4, 5], 0), [])

    def test_edge_case_n_equal_to_length(self):
        self.assertEqual(heap_queue_smallest([1, 2, 3, 4, 5], 5), [1, 2, 3, 4, 5])

    def test_edge_case_empty_list(self):
        self.assertEqual(heap_queue_smallest([], 3), [])

    def test_edge_case_n_greater_than_length(self):
        self.assertEqual(heap_queue_smallest([1, 2, 3, 4, 5], 10), [1, 2, 3, 4, 5])

    def test_edge_case_negative_n(self):
        with self.assertRaises(ValueError):
            heap_queue_smallest([1, 2, 3, 4, 5], -3)

    def test_edge_case_negative_num(self):
        with self.assertRaises(ValueError):
            heap_queue_smallest([1, 2, 3, 4, 5], 3, -1)
