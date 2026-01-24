import unittest
from mbpp_496_code import heap_queue_smallest

class TestHeapQueueSmallest(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(heap_queue_smallest([1, 2, 3, 4, 5], 3), [1, 2, 3])

    def test_edge_case(self):
        self.assertEqual(heap_queue_smallest([1, 2, 3, 4, 5], 5), [1, 2, 3, 4, 5])

    def test_edge_case2(self):
        self.assertEqual(heap_queue_smallest([1, 2, 3, 4, 5], 0), [])

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            heap_queue_smallest('abc', 3)

    def test_invalid_input2(self):
        with self.assertRaises(TypeError):
            heap_queue_smallest([1, 2, 3], 'a')

    def test_invalid_input3(self):
        with self.assertRaises(TypeError):
            heap_queue_smallest([1, 2, 3], -1)
