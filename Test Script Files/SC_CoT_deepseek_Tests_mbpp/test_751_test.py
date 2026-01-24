import unittest
from mbpp_751_code import check_min_heap

class TestCheckMinHeap(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(check_min_heap([1, 2, 3, 4, 5, 6, 7], 0))

    def test_edge_case_single_element(self):
        self.assertTrue(check_min_heap([1], 0))

    def test_edge_case_empty_array(self):
        self.assertTrue(check_min_heap([], 0))

    def test_edge_case_two_elements(self):
        self.assertTrue(check_min_heap([1, 2], 0))

    def test_corner_case_equal_elements(self):
        self.assertTrue(check_min_heap([1, 1, 1, 1], 0))

    def test_corner_case_large_array(self):
        self.assertTrue(check_min_heap(list(range(1, 10001)), 0))

    def test_invalid_input_none(self):
        with self.assertRaises(TypeError):
            check_min_heap(None, 0)

    def test_invalid_input_non_list(self):
        with self.assertRaises(TypeError):
            check_min_heap("not a list", 0)

    def test_invalid_input_negative_index(self):
        with self.assertRaises(IndexError):
            check_min_heap([1, 2, 3], -1)

    def test_invalid_input_out_of_range_index(self):
        with self.assertRaises(IndexError):
            check_min_heap([1, 2, 3], 3)
