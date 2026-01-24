import unittest
from mbpp_751_code import check_min_heap

class TestCheckMinHeap(unittest.TestCase):
    def test_empty_array(self):
        self.assertTrue(check_min_heap([], 0))

    def test_single_element_array(self):
        self.assertTrue(check_min_heap([5], 0))

    def test_min_heap_property(self):
        self.assertTrue(check_min_heap([5, 2, 8, 3, 1, 6, 4], 0))

    def test_max_heap_property(self):
        self.assertFalse(check_min_heap([5, 2, 8, 3, 1, 6, 4], 0))

    def test_edge_case_left_child(self):
        self.assertTrue(check_min_heap([5, 2, 8, 3, 1, 6, 4], 1))

    def test_edge_case_right_child(self):
        self.assertTrue(check_min_heap([5, 2, 8, 3, 1, 6, 4], 3))

    def test_edge_case_last_node(self):
        self.assertTrue(check_min_heap([5, 2, 8, 3, 1, 6, 4], 6))

    def test_edge_case_last_node_left_child(self):
        self.assertTrue(check_min_heap([5, 2, 8, 3, 1, 6, 4], 5))

    def test_edge_case_last_node_right_child(self):
        self.assertTrue(check_min_heap([5, 2, 8, 3, 1, 6, 4], 6))

    def test_edge_case_last_node_left_child_right_child(self):
        self.assertTrue(check_min_heap([5, 2, 8, 3, 1, 6, 4], 5))

    def test_edge_case_last_node_right_child_right_child(self):
        self.assertTrue(check_min_heap([5, 2, 8, 3, 1, 6, 4], 6))
