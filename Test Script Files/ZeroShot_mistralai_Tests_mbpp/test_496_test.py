import unittest
from mbpp_496_code import heap_queue_smallest

class TestHeapQueueSmallest(unittest.TestCase):

    def test_empty_list(self):
        self.assertListEqual(heap_queue_smallest([], 1), [])

    def test_single_element(self):
        self.assertListEqual(heap_queue_smallest([1], 1), [1])

    def test_multiple_elements(self):
        self.assertListEqual(heap_queue_smallest([5, 2, 9, 1, 4, 3], 3), [1, 2, 3])

    def test_n_larger_than_list_length(self):
        self.assertListEqual(heap_queue_smallest([1, 2, 3], 5), [1, 2, 3])

    def test_negative_numbers(self):
        self.assertListEqual(heap_queue_smallest([-1, -2, -3, -4, -5], 3), [-1, -2, -3])
