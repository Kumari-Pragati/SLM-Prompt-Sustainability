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

    def test_error_case_non_integer_elements(self):
        with self.assertRaises(TypeError):
            check_min_heap(['1', 2, 3], 0)

    def test_error_case_negative_index(self):
        with self.assertRaises(IndexError):
            check_min_heap([1, 2, 3], -1)

    def test_error_case_index_greater_than_length(self):
        with self.assertRaises(IndexError):
            check_min_heap([1, 2, 3], 3)
