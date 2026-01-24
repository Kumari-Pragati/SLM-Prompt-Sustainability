import unittest
from mbpp_4_code import heap_queue_largest

class TestHeapQueueLargest(unittest.TestCase):

    def test_empty_list(self):
        self.assertListEqual(heap_queue_largest([], 1), [])

    def test_single_element(self):
        self.assertListEqual(heap_queue_largest([1], 1), [1])

    def test_multiple_elements(self):
        self.assertListEqual(heap_queue_largest([1, 3, 5, 7, 9], 3), [9, 7, 5])

    def test_one_larger_than_n(self):
        self.assertListEqual(heap_queue_largest([1, 3, 5, 7, 9], 2), [9, 7])

    def test_negative_numbers(self):
        self.assertListEqual(heap_queue_largest([-1, -3, -5, -7, -9], 3), [-9, -7, -5])

    def test_duplicates(self):
        self.assertListEqual(heap_queue_largest([1, 1, 3, 5, 7, 7, 9], 4), [9, 7, 7, 5])

    def test_invalid_input_n_zero(self):
        with self.assertRaises(ValueError):
            heap_queue_largest([1, 3, 5, 7, 9], 0)

    def test_invalid_input_n_negative(self):
        with self.assertRaises(ValueError):
            heap_queue_largest([1, 3, 5, 7, 9], -1)
