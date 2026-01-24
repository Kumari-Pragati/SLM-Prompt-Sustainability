import unittest
from mbpp_496_code import heap_queue_smallest

class TestHeapQueueSmallest(unittest.TestCase):

    def test_simple_input(self):
        self.assertListEqual(heap_queue_smallest([1, 2, 3, 4, 5], 2), [1, 2])
        self.assertListEqual(heap_queue_smallest([6, 7, 8, 9, 10], 3), [6, 7, 8])

    def test_edge_cases(self):
        self.assertListEqual(heap_queue_smallest([], 1), [])
        self.assertListEqual(heap_queue_smallest([1], 1), [1])
        self.assertListEqual(heap_queue_smallest([1, 2], 2), [1, 2])
        self.assertListEqual(heap_queue_smallest([1, 2, 3], 4), [1, 2, 3])
        self.assertListEqual(heap_queue_smallest([1, 2, 3], 0), [])
        self.assertListEqual(heap_queue_smallest([1, 2, 3], 5), [1, 2, 3])

    def test_complex_input(self):
        self.assertListEqual(heap_queue_smallest([100, 200, 300, 400, 500], 2), [100, 200])
        self.assertListEqual(heap_queue_smallest([-100, -200, -300, -400, -500], 2), [-500, -400])
        self.assertListEqual(heap_queue_smallest([1, 2, 2, 1, 3], 3), [1, 2, 2])
