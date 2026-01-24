import unittest
from mbpp_496_code import heap_queue_smallest

class TestHeapQueueSmallest(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(heap_queue_smallest([3, 1, 2], 2), [1, 2])

    def test_edge_case_n_equals_zero(self):
        self.assertEqual(heap_queue_smallest([3, 1, 2], 0), [])

    def test_boundary_case_n_equals_len_nums(self):
        self.assertEqual(heap_queue_smallest([3, 1, 2], 3), [1, 2, 3])

    def test_corner_case_n_greater_than_len_nums(self):
        self.assertEqual(heap_queue_smallest([3, 1, 2], 5), [1, 2, 3])

    def test_invalid_input_n_negative(self):
        with self.assertRaises(ValueError):
            heap_queue_smallest([3, 1, 2], -1)

    def test_invalid_input_n_greater_than_len_nums_with_duplicates(self):
        self.assertEqual(heap_queue_smallest([3, 1, 2, 1], 3), [1, 1, 2])
