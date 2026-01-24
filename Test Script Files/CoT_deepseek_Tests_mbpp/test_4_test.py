import unittest
from mbpp_4_code import heap_queue_largest

class TestHeapQueueLargest(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(heap_queue_largest([1, 2, 3, 4, 5], 3), [5, 4, 3])

    def test_same_numbers(self):
        self.assertEqual(heap_queue_largest([5, 5, 5, 5, 5], 3), [5, 5, 5])

    def test_large_numbers(self):
        self.assertEqual(heap_queue_largest([1000, 2000, 3000, 4000, 5000], 3), [5000, 4000, 3000])

    def test_negative_numbers(self):
        self.assertEqual(heap_queue_largest([-1, -2, -3, -4, -5], 3), [-1, -2, -3])

    def test_boundary_case(self):
        self.assertEqual(heap_queue_largest([1, 2, 3, 4, 5], 5), [5, 4, 3, 2, 1])
        self.assertEqual(heap_queue_largest([1, 2, 3, 4, 5], 0), [])

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            heap_queue_largest("1, 2, 3, 4, 5", 3)
        with self.assertRaises(TypeError):
            heap_queue_largest([1, 2, 3, 4, 5], "3")
        with self.assertRaises(ValueError):
            heap_queue_largest([1, 2, 3, 4, 5], 6)
