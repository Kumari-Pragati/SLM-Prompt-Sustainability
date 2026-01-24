import unittest
from mbpp_496_code import heap_queue_smallest

class TestHeapQueueSmallest(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertListEqual(heap_queue_smallest([1, 2, 3, 4, 5], 3), [1, 2, 3])

    def test_empty_list(self):
        self.assertListEqual(heap_queue_smallest([], 1), [])

    def test_single_element(self):
        self.assertListEqual(heap_queue_smallest([1], 1), [1])

    def test_single_element_n(self):
        self.assertListEqual(heap_queue_smallest([1], 2), [1])

    def test_one_larger_than_n(self):
        self.assertListEqual(heap_queue_smallest([1, 2, 3, 4, 5], 6), [1, 2, 3, 4, 5])

    def test_negative_numbers(self):
        self.assertListEqual(heap_queue_smallest([-1, -2, -3, -4, -5], 3), [-1, -2, -3])
