import unittest
from mbpp_4_code import heap_queue_largest

class TestHeapQueueLargest(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(heap_queue_largest([1, 2, 3, 4, 5], 3), [5, 4, 3])

    def test_edge_case(self):
        self.assertEqual(heap_queue_largest([1, 2, 3, 4, 5], 1), [5])

    def test_edge_case2(self):
        self.assertEqual(heap_queue_largest([1, 2, 3, 4, 5], 5), [5, 4, 3, 2, 1])

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            heap_queue_largest('abc', 3)

    def test_invalid_input2(self):
        with self.assertRaises(TypeError):
            heap_queue_largest([1, 2, 3], 'a')

    def test_invalid_input3(self):
        with self.assertRaises(TypeError):
            heap_queue_largest([1, 2, 3], -1)
