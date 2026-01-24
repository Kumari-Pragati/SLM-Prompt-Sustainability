import unittest
from mbpp_496_code import heap_queue_smallest

class TestHeapQueueSmallest(unittest.TestCase):

    def test_empty_list(self):
        with self.assertRaises(ValueError):
            heap_queue_smallest([], 1)

    def test_single_element(self):
        self.assertEqual(heap_queue_smallest([1], 1), [1])

    def test_single_element_n(self):
        self.assertEqual(heap_queue_smallest([1], 2), [1])

    def test_multiple_elements(self):
        self.assertEqual(heap_queue_smallest([1, 5, 3, 4, 2], 3), [1, 2, 3])

    def test_multiple_elements_n_greater_than_list_size(self):
        self.assertEqual(heap_queue_smallest([1, 5, 3, 4, 2], 6), [1, 2, 3, 4, 5])

    def test_negative_numbers(self):
        self.assertEqual(heap_queue_smallest([-1, -5, -3, -4, -2], 3), [-1, -2, -3])

    def test_duplicates(self):
        self.assertEqual(heap_queue_smallest([1, 1, 5, 3, 4, 2], 3), [1, 2, 3])
