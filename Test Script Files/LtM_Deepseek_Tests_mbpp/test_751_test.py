import unittest
from mbpp_751_code import check_min_heap

class TestCheckMinHeap(unittest.TestCase):

    def test_simple_case(self):
        self.assertTrue(check_min_heap([1, 2, 3, 4, 5, 6, 7], 0))

    def test_edge_case_empty_array(self):
        self.assertTrue(check_min_heap([], 0))

    def test_edge_case_single_element(self):
        self.assertTrue(check_min_heap([1], 0))

    def test_boundary_case_minimum_value(self):
        self.assertTrue(check_min_heap([0, 1, 2, 3, 4, 5, 6, 7], 0))

    def test_boundary_case_maximum_value(self):
        self.assertFalse(check_min_heap([1000000000, 1, 2, 3, 4, 5, 6, 7], 0))

    def test_complex_case_invalid_min_heap(self):
        self.assertFalse(check_min_heap([2, 3, 1, 5, 6, 7, 4], 0))
