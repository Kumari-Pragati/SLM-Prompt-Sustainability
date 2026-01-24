import unittest
from mbpp_4_code import heap_queue_largest

class TestHeapQueueLargest(unittest.TestCase):

    def test_empty_list(self):
        self.assertListEqual(heap_queue_largest([], 1), [])

    def test_single_element(self):
        self.assertListEqual(heap_queue_largest([1], 1), [1])

    def test_multiple_elements(self):
        self.assertListEqual(heap_queue_largest([1, 2, 3, 4, 5], 3), [4, 3, 2])

    def test_n_larger_than_len(self):
        self.assertListEqual(heap_queue_largest([1, 2, 3, 4, 5], 6), [1, 2, 3, 4, 5])

    def test_negative_numbers(self):
        self.assertListEqual(heap_queue_largest([-1, -2, -3, -4, -5], 3), [-1, -2, -3])
