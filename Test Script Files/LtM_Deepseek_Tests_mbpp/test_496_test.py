import unittest
from mbpp_496_code import heap_queue_smallest

class TestHeapQueueSmallest(unittest.TestCase):

    def test_simple_case(self):
        self.assertEqual(heap_queue_smallest([3, 1, 2], 2), [1, 2])

    def test_empty_list(self):
        self.assertEqual(heap_queue_smallest([], 2), [])

    def test_single_element(self):
        self.assertEqual(heap_queue_smallest([5], 1), [5])

    def test_same_elements(self):
        self.assertEqual(heap_queue_smallest([2, 2, 2], 2), [2, 2])

    def test_large_numbers(self):
        self.assertEqual(heap_queue_smallest([100, 200, 300], 2), [100, 200])

    def test_negative_numbers(self):
        self.assertEqual(heap_queue_smallest([-1, -2, -3], 2), [-3, -2])

    def test_large_n(self):
        self.assertEqual(heap_queue_smallest([1, 2, 3, 4, 5], 6), [1, 2, 3, 4, 5])

    def test_n_equals_zero(self):
        self.assertEqual(heap_queue_smallest([1, 2, 3], 0), [])
