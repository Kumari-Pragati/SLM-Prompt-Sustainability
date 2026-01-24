import unittest
from mbpp_854_code import raw_heap

class TestRawHeap(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(raw_heap([1, 2, 3]), [1, 2, 3])
        self.assertEqual(raw_heap([3, 2, 1]), [1, 2, 3])
        self.assertEqual(raw_heap([-1, -2, -3]), [-3, -2, -1])

    def test_empty_input(self):
        self.assertEqual(raw_heap([]), [])

    def test_single_input(self):
        self.assertEqual(raw_heap([0]), [0])

    def test_negative_numbers(self):
        self.assertEqual(raw_heap([-5, -3, -1, 1, 3, 5]), [-5, -3, -1, 1, 3, 5])

    def test_duplicate_numbers(self):
        self.assertEqual(raw_heap([1, 1, 2, 2, 3]), [1, 1, 2, 2, 3])

    def test_large_numbers(self):
        self.assertEqual(raw_heap([1000000, 999999, 999998]), [999998, 999999, 1000000])
