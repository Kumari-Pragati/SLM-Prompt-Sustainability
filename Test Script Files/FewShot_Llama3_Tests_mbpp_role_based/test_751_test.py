import unittest
from mbpp_751_code import check_min_heap

class TestCheckMinHeap(unittest.TestCase):
    def test_empty_array(self):
        self.assertFalse(check_min_heap([], 0))

    def test_single_element_array(self):
        self.assertTrue(check_min_heap([5], 0))

    def test_min_heap_array(self):
        self.assertTrue(check_min_heap([5, 2, 8, 3, 1, 4], 0))

    def test_non_min_heap_array(self):
        self.assertFalse(check_min_heap([5, 2, 8, 3, 1, 4, 6], 0))

    def test_array_with_duplicates(self):
        self.assertTrue(check_min_heap([5, 2, 8, 3, 1, 4, 4], 0))

    def test_array_with_duplicates_and_non_min_heap(self):
        self.assertFalse(check_min_heap([5, 2, 8, 3, 1, 4, 6, 6], 0))

    def test_array_with_duplicates_and_non_min_heap_and_edge_case(self):
        self.assertFalse(check_min_heap([5, 2, 8, 3, 1, 4, 6, 6, 7], 0))
