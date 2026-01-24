import unittest
from mbpp_751_code import check_min_heap

class TestCheckMinHeap(unittest.TestCase):
    def test_typical_case(self):
        self.assertTrue(check_min_heap([1, 2, 3, 4, 5], 0))

    def test_edge_case_empty_array(self):
        self.assertTrue(check_min_heap([], 0))

    def test_edge_case_single_element_array(self):
        self.assertTrue(check_min_heap([1], 0))

    def test_edge_case_two_element_array(self):
        self.assertTrue(check_min_heap([1, 2], 0))

    def test_edge_case_three_element_array(self):
        self.assertTrue(check_min_heap([1, 2, 3], 0))

    def test_edge_case_max_heap(self):
        self.assertTrue(check_min_heap([5, 2, 8, 3, 1, 6, 4], 0))

    def test_edge_case_min_heap(self):
        self.assertTrue(check_min_heap([1, 2, 3, 4, 5, 6, 7], 0))

    def test_edge_case_invalid_input(self):
        with self.assertRaises(IndexError):
            check_min_heap([1, 2, 3], -1)

    def test_edge_case_invalid_input2(self):
        with self.assertRaises(IndexError):
            check_min_heap([1, 2, 3], len([1, 2, 3]) + 1)
