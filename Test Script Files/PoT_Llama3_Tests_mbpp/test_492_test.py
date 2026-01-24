import unittest
from mbpp_492_code import binary_search

class TestBinarySearch(unittest.TestCase):

    def test_found(self):
        self.assertTrue(binary_search([1,2,3,4,5], 3))

    def test_not_found(self):
        self.assertFalse(binary_search([1,2,3,4,5], 6))

    def test_edge_case_found(self):
        self.assertTrue(binary_search([1,2,3,4,5], 2))

    def test_edge_case_not_found(self):
        self.assertFalse(binary_search([1,2,3,4,5], 0))

    def test_empty_list(self):
        self.assertFalse(binary_search([], 1))

    def test_single_element_list(self):
        self.assertTrue(binary_search([1], 1))

    def test_empty_list_with_item(self):
        self.assertFalse(binary_search([], 1))

    def test_single_element_list_with_item(self):
        self.assertTrue(binary_search([1], 1))

    def test_binary_search_with_duplicates(self):
        self.assertTrue(binary_search([1,2,2,3,4,5], 2))

    def test_binary_search_with_duplicates_not_found(self):
        self.assertFalse(binary_search([1,2,2,3,4,5], 6))
