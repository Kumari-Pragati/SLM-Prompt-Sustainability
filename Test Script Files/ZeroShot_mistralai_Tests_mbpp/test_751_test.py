import unittest
from mbpp_751_code import check_min_heap

class TestCheckMinHeap(unittest.TestCase):

    def test_empty_list(self):
        self.assertTrue(check_min_heap([], 0))

    def test_single_element(self):
        self.assertTrue(check_min_heap([1], 0))

    def test_min_heap_small(self):
        self.assertTrue(check_min_heap([1, 2, 3, 4, 5], 0))

    def test_min_heap_large(self):
        self.assertTrue(check_min_heap([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 0))

    def test_not_min_heap_small(self):
        self.assertFalse(check_min_heap([5, 2, 3, 4, 1], 0))

    def test_not_min_heap_large(self):
        self.assertFalse(check_min_heap([10, 20, 30, 40, 50, 60, 70, 80, 90, 1], 0))

    def test_invalid_index(self):
        self.assertRaises(IndexError, check_min_heap, [1, 2, 3], 4)
