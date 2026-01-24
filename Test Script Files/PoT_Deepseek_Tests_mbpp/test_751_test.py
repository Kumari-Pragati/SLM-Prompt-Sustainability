import unittest
from mbpp_751_code import check_min_heap

class TestCheckMinHeap(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(check_min_heap([1, 2, 3, 4, 5, 6, 7], 0))

    def test_edge_case_single_element(self):
        self.assertTrue(check_min_heap([1], 0))

    def test_boundary_case_empty_array(self):
        self.assertTrue(check_min_heap([], 0))

    def test_corner_case_one_level_min_heap(self):
        self.assertTrue(check_min_heap([1, 2, 3], 0))

    def test_typical_case_two_level_min_heap(self):
        self.assertTrue(check_min_heap([1, 2, 3, 4, 5, 6], 0))

    def test_edge_case_two_level_min_heap_with_equal_elements(self):
        self.assertTrue(check_min_heap([1, 1, 2, 3, 4, 5], 0))

    def test_corner_case_two_level_min_heap_with_one_element(self):
        self.assertTrue(check_min_heap([1, 2, 3, 4, 5], 0))

    def test_invalid_case_non_heap_structure(self):
        self.assertFalse(check_min_heap([3, 1, 2, 5, 4, 6], 0))
