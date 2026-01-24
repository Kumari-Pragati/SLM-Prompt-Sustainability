import unittest
from mbpp_492_code import binary_search

class TestBinarySearch(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertTrue(binary_search([1, 2, 3, 4, 5], 4))

    def test_edge_case_item_not_in_list(self):
        self.assertFalse(binary_search([1, 2, 3, 4, 5], 10))

    def test_boundary_case_empty_list(self):
        self.assertFalse(binary_search([], 4))

    def test_boundary_case_single_element_list(self):
        self.assertTrue(binary_search([4], 4))
        self.assertFalse(binary_search([4], 3))

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            binary_search("not a list", 4)
