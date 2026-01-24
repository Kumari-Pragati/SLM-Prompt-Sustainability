import unittest
from mbpp_4_code import heap_queue_largest

class TestHeapQueueLargest(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(heap_queue_largest([1, 2, 3, 4, 5], 3), [5, 4, 3])

    def test_edge_case_n_equal_to_length(self):
        self.assertEqual(heap_queue_largest([1, 2, 3, 4, 5], 5), [5, 4, 3, 2, 1])

    def test_edge_case_n_greater_than_length(self):
        self.assertRaises(ValueError, heap_queue_largest, [1, 2, 3, 4, 5], 10)

    def test_edge_case_empty_list(self):
        self.assertEqual(heap_queue_largest([], 1), [])

    def test_edge_case_n_equal_to_zero(self):
        self.assertEqual(heap_queue_largest([1, 2, 3, 4, 5], 0), [])

    def test_edge_case_negative_n(self):
        self.assertRaises(ValueError, heap_queue_largest, [1, 2, 3, 4, 5], -1)
