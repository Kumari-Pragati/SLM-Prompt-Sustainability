import unittest
from mbpp_496_code import heap_queue_smallest

class TestHeapQueueSmallest(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(heap_queue_smallest([1, 2, 3, 4, 5], 3), [1, 2, 3])
        self.assertEqual(heap_queue_smallest([5, 3, 1, 4, 2], 3), [1, 2, 3])
        self.assertEqual(heap_queue_smallest([10, 20, 30, 40, 50], 2), [10, 20])

    def test_edge_cases(self):
        self.assertEqual(heap_queue_smallest([], 1), [])
        self.assertEqual(heap_queue_smallest([1], 1), [1])
        self.assertEqual(heap_queue_smallest([1, 2], 2), [1, 2])
        self.assertEqual(heap_queue_smallest([1, 2, 3], 4), [1, 2, 3])
        self.assertEqual(heap_queue_smallest([1, 2, 3], 0), [])
        self.assertEqual(heap_queue_smallest([1, 2, 3], 5), [1, 2, 3])

    def test_negative_numbers(self):
        self.assertEqual(heap_queue_smallest([-1, -2, -3], 2), [-3, -2])

    def test_floats(self):
        self.assertEqual(heap_queue_smallest([1.1, 2.2, 3.3], 2), [1.1, 2.2])

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            heap_queue_smallest('not a list', 1)
        with self.assertRaises(TypeError):
            heap_queue_smallest([1], 'not an integer')
