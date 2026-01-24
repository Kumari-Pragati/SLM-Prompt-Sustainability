import unittest
from mbpp_751_code import check_min_heap

class TestCheckMinHeap(unittest.TestCase):
    def test_simple(self):
        self.assertTrue(check_min_heap([1, 2, 3, 4, 5], 0))
        self.assertTrue(check_min_heap([1, 2, 3, 4, 5], 1))
        self.assertTrue(check_min_heap([1, 2, 3, 4, 5], 2))
        self.assertTrue(check_min_heap([1, 2, 3, 4, 5], 3))
        self.assertTrue(check_min_heap([1, 2, 3, 4, 5], 4))

    def test_edge_cases(self):
        self.assertTrue(check_min_heap([], 0))
        self.assertTrue(check_min_heap([1], 0))
        self.assertTrue(check_min_heap([1, 2], 0))
        self.assertTrue(check_min_heap([1, 2, 3], 0))
        self.assertTrue(check_min_heap([1, 2, 3], 1))
        self.assertTrue(check_min_heap([1, 2, 3], 2))
        self.assertFalse(check_min_heap([1, 2, 3], 3))

        self.assertTrue(check_min_heap([1, 2, 3], 4))
        self.assertFalse(check_min_heap([1, 2, 3], 5))

    def test_complex(self):
        self.assertTrue(check_min_heap([1, 2, 3, 4, 5, 6], 0))
        self.assertTrue(check_min_heap([1, 2, 3, 4, 5, 6], 1))
        self.assertTrue(check_min_heap([1, 2, 3, 4, 5, 6], 2))
        self.assertTrue(check_min_heap([1, 2, 3, 4, 5, 6], 3))
        self.assertTrue(check_min_heap([1, 2, 3, 4, 5, 6], 4))
        self.assertTrue(check_min_heap([1, 2, 3, 4, 5, 6], 5))
        self.assertFalse(check_min_heap([1, 2, 3, 4, 5, 6], 6))

        self.assertTrue(check_min_heap([1, 2, 3, 4, 5, 6], 7))
        self.assertFalse(check_min_heap([1, 2, 3, 4, 5, 6], 8))
