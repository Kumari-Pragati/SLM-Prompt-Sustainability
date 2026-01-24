import unittest
from mbpp_4_code import heap_queue_largest

class TestHeapQueueLargest(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(heap_queue_largest([3, 1, 4, 1, 5, 9, 2, 6, 5, 3], 3), [9, 6, 5])

    def test_edge_case_n_equals_zero(self):
        self.assertEqual(heap_queue_largest([3, 1, 4, 1, 5, 9, 2, 6, 5, 3], 0), [])

    def test_edge_case_n_equals_length_of_nums(self):
        self.assertEqual(heap_queue_largest([3, 1, 4, 1, 5, 9, 2, 6, 5, 3], 10), [9, 6, 5, 4, 3, 3, 2, 1, 1, 5])

    def test_boundary_case_n_greater_than_length_of_nums(self):
        self.assertEqual(heap_queue_largest([3, 1, 4, 1, 5, 9, 2, 6, 5, 3], 11), [9, 6, 5, 4, 3, 3, 2, 1, 1, 5])

    def test_corner_case_empty_nums(self):
        self.assertEqual(heap_queue_largest([], 3), [])

    def test_corner_case_negative_numbers(self):
        self.assertEqual(heap_queue_largest([-3, -1, -4, -1, -5, -9, -2, -6, -5, -3], 3), [-1, -2, -3])

    def test_corner_case_duplicate_numbers(self):
        self.assertEqual(heap_queue_largest([3, 3, 4, 4, 5, 5, 2, 2, 1, 1], 3), [5, 4, 3])
