import unittest
from mbpp_751_code import check_min_heap

class TestCheckMinHeap(unittest.TestCase):
    def test_typical_case(self):
        self.assertTrue(check_min_heap([1, 2, 3, 4, 5, 6, 7], 0))

    def test_edge_case(self):
        self.assertTrue(check_min_heap([1], 0))

    def test_boundary_case(self):
        self.assertTrue(check_min_heap([], 0))

    def test_invalid_input(self):
        with self.assertRaises(IndexError):
            check_min_heap([1, 2, 3, 4, 5, 6, 7], 10)

    def test_non_heap_case(self):
        self.assertFalse(check_min_heap([3, 2, 1, 4, 5, 6, 7], 0))
