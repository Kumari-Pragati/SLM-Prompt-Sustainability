import unittest
from mbpp_4_code import heap_queue_largest

class TestHeapQueueLargest(unittest.TestCase):

    def test_simple_case(self):
        self.assertEqual(heap_queue_largest([3, 1, 4, 1, 5, 9, 2, 6, 5, 3], 3), [9, 6, 5])

    def test_empty_list(self):
        self.assertEqual(heap_queue_largest([], 3), [])

    def test_large_n(self):
        self.assertEqual(heap_queue_largest([3, 1, 4, 1, 5, 9, 2, 6, 5, 3], 10), [9, 6, 5, 5, 4, 3, 3, 2, 1, 1])

    def test_small_n(self):
        self.assertEqual(heap_queue_largest([3, 1, 4, 1, 5, 9, 2, 6, 5, 3], 1), [9])

    def test_negative_numbers(self):
        self.assertEqual(heap_queue_largest([-3, -1, -4, -1, -5, -9, -2, -6, -5, -3], 3), [-1, -2, -3])

    def test_same_numbers(self):
        self.assertEqual(heap_queue_largest([3, 3, 3, 3, 3, 3, 3, 3, 3, 3], 3), [3, 3, 3])

    def test_max_values(self):
        self.assertEqual(heap_queue_largest([float('inf')] * 10, 3), [float('inf'), float('inf'), float('inf')])

    def test_min_values(self):
        self.assertEqual(heap_queue_largest([float('-inf')] * 10, 3), [float('-inf'), float('-inf'), float('-inf')])
