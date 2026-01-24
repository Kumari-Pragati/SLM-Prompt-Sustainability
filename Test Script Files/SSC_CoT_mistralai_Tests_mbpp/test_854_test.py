import unittest
from mbpp_854_code import raw_heap

class TestRawHeap(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(raw_heap([3, 5, 1, 7, 9]), [1, 3, 5, 7, 9])
        self.assertEqual(raw_heap([1]), [1])
        self.assertEqual(raw_heap([1, 2, 3]), [1, 2, 3])

    def test_edge_cases(self):
        self.assertEqual(raw_heap([]), [])
        self.assertEqual(raw_heap([float('inf'), float('inf'), float('inf')]), [float('inf'), float('inf'), float('inf')])
        self.assertEqual(raw_heap([float('-inf'), float('-inf'), float('-inf')]), [float('-inf'), float('-inf'), float('-inf')])

    def test_negative_numbers(self):
        self.assertEqual(raw_heap([-3, -5, -1, -7, -9]), [-3, -5, -1, -7, -9])
        self.assertEqual(raw_heap([-1]), [-1])
        self.assertEqual(raw_heap([-1, -2, -3]), [-1, -2, -3])

    def test_mixed_numbers(self):
        self.assertEqual(raw_heap([1, -2, 3, -4, 5]), [1, -2, 3, -4, 5])
        self.assertEqual(raw_heap([-1, 0, 1]), [-1, 0, 1])
        self.assertEqual(raw_heap([-1, 0, 1, -2, 0]), [-1, 0, 1, -2, 0])
