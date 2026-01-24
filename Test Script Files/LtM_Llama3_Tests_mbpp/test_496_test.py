import unittest
from mbpp_496_code import heap_queue_smallest

class TestHeapQueueSmallest(unittest.TestCase):
    def test_simple_input(self):
        self.assertEqual(heap_queue_smallest([1, 2, 3, 4, 5], 3), [1, 2, 3])

    def test_edge_case_empty_input(self):
        self.assertEqual(heap_queue_smallest([], 1), [])

    def test_edge_case_single_element_input(self):
        self.assertEqual(heap_queue_smallest([1], 1), [1])

    def test_edge_case_max_input(self):
        self.assertEqual(heap_queue_smallest([1, 2, 3, 4, 5], 5), [1, 2, 3, 4, 5])

    def test_edge_case_min_input(self):
        self.assertEqual(heap_queue_smallest([5, 4, 3, 2, 1], 3), [1, 2, 3])

    def test_edge_case_invalid_input(self):
        with self.assertRaises(TypeError):
            heap_queue_smallest('abc', 3)

    def test_edge_case_invalid_input_type(self):
        with self.assertRaises(TypeError):
            heap_queue_smallest([1, 2, 3], 'n')

    def test_edge_case_invalid_input_value(self):
        with self.assertRaises(TypeError):
            heap_queue_smallest([1, 2, 3], -1)
