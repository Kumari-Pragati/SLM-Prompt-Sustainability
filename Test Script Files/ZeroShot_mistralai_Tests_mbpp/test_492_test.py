import unittest
from mbpp_492_code import binary_search

class TestBinarySearch(unittest.TestCase):

    def test_empty_list(self):
        self.assertFalse(binary_search([], 1))

    def test_single_element(self):
        self.assertFalse(binary_search([2], 1))
        self.assertTrue(binary_search([1], 1))

    def test_not_found(self):
        self.assertFalse(binary_search([1, 2, 3, 4, 5], 6))

    def test_found(self):
        self.assertTrue(binary_search([1, 2, 3, 4, 5], 3))
        self.assertTrue(binary_search([1, 2, 3, 4, 5], 5))

    def test_duplicates(self):
        self.assertTrue(binary_search([1, 1, 2, 2, 3, 3, 4, 4, 5], 1))
        self.assertTrue(binary_search([1, 1, 2, 2, 3, 3, 4, 4, 5], 3))
        self.assertTrue(binary_search([1, 1, 2, 2, 3, 3, 4, 4, 5], 4))
        self.assertTrue(binary_search([1, 1, 2, 2, 3, 3, 4, 4, 5], 5))
