import unittest
from mbpp_4_code import heap_queue_largest

class TestHeapQueueLargest(unittest.TestCase):

    def test_normal_inputs(self):
        self.assertEqual(heap_queue_largest([1, 2, 3, 4, 5], 3), [5, 4, 3])
        self.assertEqual(heap_queue_largest([-1, -2, -3, -4, -5], 3), [-5, -4, -3])
        self.assertEqual(heap_queue_largest([1, 1, 1, 1, 1], 1), [1])

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(heap_queue_largest([], 1), [])
        self.assertEqual(heap_queue_largest([1], 1), [1])
        self.assertEqual(heap_queue_largest([1, 2], 2), [2, 1])
        self.assertEqual(heap_queue_largest([1, 2, 3], 4), [3, 2, 1])
        self.assertEqual(heap_queue_largest([1, 2, 3, 4, 5], 6), [5, 4, 3, 2, 1])

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, heap_queue_largest, 'string', 1)
        self.assertRaises(TypeError, heap_queue_largest, [1, 2], 'int')
        self.assertRaises(ValueError, heap_queue_largest, [1, 2], -1)
