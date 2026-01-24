import unittest
from mbpp_4_code import heap_queue_largest

class TestHeapQueueLargest(unittest.TestCase):

    def test_typical_case(self):
        self.assertListEqual(heap_queue_largest([1, 2, 3, 4, 5], 3), [5, 4, 3])
        self.assertListEqual(heap_queue_largest([10, 20, 30, 40, 50], 2), [50, 40])
        self.assertListEqual(heap_queue_largest([-1, -2, -3, -4, -5], 2), [-1, -2])

    def test_edge_case_empty(self):
        self.assertListEqual(heap_queue_largest([], 1), [])

    def test_edge_case_single_element(self):
        self.assertListEqual(heap_queue_largest([1], 1), [1])

    def test_edge_case_n_larger_than_len(self):
        self.assertListEqual(heap_queue_largest([1, 2, 3], 5), [1, 2, 3])

    def test_edge_case_n_equal_len(self):
        self.assertListEqual(heap_queue_largest([1, 2, 3], 4), [1, 2, 3])

    def test_edge_case_negative_n(self):
        self.assertRaises(ValueError, heap_queue_largest, [1, 2, 3], -1)
