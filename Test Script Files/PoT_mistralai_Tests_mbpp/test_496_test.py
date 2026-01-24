import unittest
from mbpp_496_code import heap_queue_smallest

class TestHeapQueueSmallest(unittest.TestCase):

    def test_typical_case(self):
        self.assertListEqual(heap_queue_smallest([1, 2, 3, 4, 5], 3), [1, 2, 3])
        self.assertListEqual(heap_queue_smallest([6, 5, 4, 3, 2, 1], 4), [1, 2, 3, 4])

    def test_edge_case_empty_list(self):
        self.assertListEqual(heap_queue_smallest([], 1), [])

    def test_edge_case_single_element(self):
        self.assertListEqual(heap_queue_smallest([1], 1), [1])

    def test_edge_case_single_element_n(self):
        self.assertListEqual(heap_queue_smallest([1], 2), [1])

    def test_edge_case_n_greater_than_len(self):
        self.assertListEqual(heap_queue_smallest([1, 2, 3], 5), [1, 2, 3])

    def test_corner_case_duplicates(self):
        self.assertListEqual(heap_queue_smallest([1, 1, 2, 3], 2), [1, 1])
