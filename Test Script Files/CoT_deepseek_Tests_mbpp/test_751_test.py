import unittest
from mbpp_751_code import check_min_heap

class TestCheckMinHeap(unittest.TestCase):

    def test_empty_array(self):
        self.assertTrue(check_min_heap([], 0))

    def test_single_element(self):
        self.assertTrue(check_min_heap([1], 0))

    def test_valid_min_heap(self):
        self.assertTrue(check_min_heap([1, 2, 3, 4, 5, 6, 7], 0))

    def test_invalid_min_heap(self):
        self.assertFalse(check_min_heap([1, 2, 3, 4, 5, 6, 7, 8], 0))

    def test_large_min_heap(self):
        self.assertTrue(check_min_heap(list(range(1, 1000)), 0))

    def test_negative_numbers_min_heap(self):
        self.assertTrue(check_min_heap([-1, -2, -3, -4, -5, -6, -7], 0))

    def test_mixed_numbers_min_heap(self):
        self.assertFalse(check_min_heap([1, -2, 3, -4, 5, -6, 7], 0))

    def test_invalid_index(self):
        with self.assertRaises(IndexError):
            check_min_heap([1, 2, 3, 4, 5, 6, 7], 10)
