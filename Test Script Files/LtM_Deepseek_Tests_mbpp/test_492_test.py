import unittest
from mbpp_492_code import binary_search

class TestBinarySearch(unittest.TestCase):

    def test_simple_case(self):
        self.assertTrue(binary_search([1, 2, 3, 4, 5], 4))

    def test_edge_case_empty_list(self):
        self.assertFalse(binary_search([], 4))

    def test_edge_case_single_element(self):
        self.assertTrue(binary_search([5], 5))
        self.assertFalse(binary_search([5], 4))

    def test_edge_case_minimum_maximum_values(self):
        self.assertTrue(binary_search([1, 2, 3, 4, 5], 1))
        self.assertTrue(binary_search([1, 2, 3, 4, 5], 5))

    def test_complex_case_duplicates(self):
        self.assertTrue(binary_search([1, 2, 2, 3, 4, 5], 2))

    def test_complex_case_not_found(self):
        self.assertFalse(binary_search([1, 2, 3, 4, 5], 6))
