import unittest
from mbpp_492_code import binary_search

class TestBinarySearch(unittest.TestCase):

    def test_binary_search_found(self):
        self.assertTrue(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9], 5))

    def test_binary_search_not_found(self):
        self.assertFalse(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9], 10))

    def test_binary_search_empty_list(self):
        self.assertFalse(binary_search([], 5))

    def test_binary_search_single_element(self):
        self.assertTrue(binary_search([5], 5))
        self.assertFalse(binary_search([5], 10))

    def test_binary_search_duplicate_elements(self):
        self.assertTrue(binary_search([1, 2, 3, 4, 5, 5, 6, 7, 8, 9], 5))
