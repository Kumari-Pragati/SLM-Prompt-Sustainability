import unittest
from mbpp_496_code import heap_queue_smallest

class TestHeapQueueSmallest(unittest.TestCase):
    def test_typical_case(self):
        self.assertListEqual(heap_queue_smallest([1, 2, 3, 4, 5], 3), [1, 2, 3])
        self.assertListEqual(heap_queue_smallest([10, 20, 30, 40, 50], 2), [10, 20])
        self.assertListEqual(heap_queue_smallest([-10, -20, -30, -40, -50], 2), [-50, -40])

    def test_edge_case_empty_list(self):
        self.assertListEqual(heap_queue_smallest([], 1), [])

    def test_edge_case_single_element(self):
        self.assertListEqual(heap_queue_smallest([1], 1), [1])

    def test_edge_case_single_element_n_greater_than_list_size(self):
        self.assertListEqual(heap_queue_smallest([1], 2), [1])

    def test_edge_case_negative_n(self):
        with self.assertRaises(ValueError):
            heap_queue_smallest([1, 2, 3], -1)

    def test_invalid_input_non_iterable(self):
        with self.assertRaises(TypeError):
            heap_queue_smallest('abc', 1)
