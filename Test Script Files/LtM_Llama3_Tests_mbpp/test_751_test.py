import unittest
from mbpp_751_code import check_min_heap

class TestCheckMinHeap(unittest.TestCase):
    def test_simple_valid_heap(self):
        self.assertTrue(check_min_heap([1, 2, 3, 4, 5], 0))

    def test_edge_empty_input(self):
        self.assertTrue(check_min_heap([], 0))

    def test_edge_single_element_input(self):
        self.assertTrue(check_min_heap([1], 0))

    def test_edge_two_elements_input(self):
        self.assertTrue(check_min_heap([1, 2], 0))

    def test_edge_three_elements_input(self):
        self.assertTrue(check_min_heap([1, 2, 3], 0))

    def test_edge_max_heap_input(self):
        self.assertTrue(check_min_heap([5, 4, 3, 2, 1], 0))

    def test_edge_min_heap_input(self):
        self.assertTrue(check_min_heap([1, 2, 3, 4, 5], 0))

    def test_edge_invalid_input(self):
        with self.assertRaises(IndexError):
            check_min_heap([1, 2, 3], 5)

    def test_edge_invalid_input2(self):
        with self.assertRaises(IndexError):
            check_min_heap([1, 2, 3], -1)
