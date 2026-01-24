import unittest
from mbpp_751_code import check_min_heap

class TestCheckMinHeap(unittest.TestCase):

    def test_empty_list(self):
        self.assertTrue(check_min_heap([], 0))

    def test_single_element(self):
        self.assertTrue(check_min_heap([1], 0))

    def test_two_elements(self):
        self.assertTrue(check_min_heap([1, 2], 0))

    def test_typical_min_heap(self):
        self.assertTrue(check_min_heap([1, 3, 2], 0))
        self.assertTrue(check_min_heap([1, 3, 2], 1))
        self.assertTrue(check_min_heap([1, 3, 2], 2))

    def test_max_depth(self):
        self.assertTrue(check_min_heap([1, 3, 2, 4, 5], 0))
        self.assertTrue(check_min_heap([1, 3, 2, 4, 5], 1))
        self.assertTrue(check_min_heap([1, 3, 2, 4, 5], 2))
        self.assertTrue(check_min_heap([1, 3, 2, 4, 5], 3))
        self.assertTrue(check_min_heap([1, 3, 2, 4, 5], 4))

    def test_invalid_index(self):
        self.assertRaises(IndexError, check_min_heap, [1, 3, 2], len([1, 3, 2]) + 1)

    def test_non_min_heap(self):
        self.assertFalse(check_min_heap([3, 1, 2], 0))
        self.assertFalse(check_min_heap([3, 1, 2], 1))
        self.assertFalse(check_min_heap([3, 1, 2], 2))
