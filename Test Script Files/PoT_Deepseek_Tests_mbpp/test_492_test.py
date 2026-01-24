import unittest
from mbpp_492_code import binary_search

class TestBinarySearch(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(binary_search([1, 2, 3, 4, 5], 4))

    def test_edge_case_empty_list(self):
        self.assertFalse(binary_search([], 4))

    def test_boundary_case_single_element(self):
        self.assertTrue(binary_search([4], 4))
        self.assertFalse(binary_search([4], 3))

    def test_corner_case_duplicate_elements(self):
        self.assertTrue(binary_search([1, 2, 2, 3, 4, 5], 2))

    def test_corner_case_first_element(self):
        self.assertTrue(binary_search([1, 2, 3, 4, 5], 1))

    def test_corner_case_last_element(self):
        self.assertTrue(binary_search([1, 2, 3, 4, 5], 5))

    def test_invalid_case_item_not_in_list(self):
        self.assertFalse(binary_search([1, 2, 3, 4, 5], 6))
