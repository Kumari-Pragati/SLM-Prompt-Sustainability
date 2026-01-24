import unittest
from mbpp_4_code import heap_queue_largest

class TestHeapQueueLargest(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(heap_queue_largest([1, 2, 3, 4, 5], 3), [5, 4, 3])

    def test_edge_case_empty_input(self):
        self.assertEqual(heap_queue_largest([], 3), [])

    def test_edge_case_single_element_input(self):
        self.assertEqual(heap_queue_largest([1], 1), [1])

    def test_edge_case_max_input(self):
        self.assertEqual(heap_queue_largest([1, 2, 3, 4, 5], 5), [5, 4, 3, 2, 1])

    def test_edge_case_min_input(self):
        self.assertEqual(heap_queue_largest([5, 4, 3, 2, 1], 3), [5, 4, 3])

    def test_edge_case_invalid_input(self):
        with self.assertRaises(TypeError):
            heap_queue_largest("abc", 3)
