import unittest
from mbpp_4_code import heap_queue_largest

class TestHeapQueueLargest(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(heap_queue_largest([1, 2, 3, 4, 5], 3), [5, 4, 3])

    def test_single_element(self):
        self.assertEqual(heap_queue_largest([1], 1), [1])

    def test_empty_list(self):
        self.assertListEqual(heap_queue_largest([], 1), [])

    def test_negative_n(self):
        with self.assertRaises(ValueError):
            heap_queue_largest([1, 2, 3], -1)

    def test_larger_n_than_list_length(self):
        with self.assertRaises(ValueError):
            heap_queue_largest([1, 2, 3], 4)
