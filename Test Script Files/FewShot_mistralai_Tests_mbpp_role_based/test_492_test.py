import unittest
from mbpp_492_code import binary_search

class TestBinarySearch(unittest.TestCase):
    def test_found_in_list(self):
        self.assertTrue(binary_search([1, 2, 3, 4, 5], 3))

    def test_not_found_in_list(self):
        self.assertFalse(binary_search([1, 2, 3, 4, 5], 6))

    def test_empty_list(self):
        self.assertFalse(binary_search([]))

    def test_single_element_list(self):
        self.assertFalse(binary_search([1]))

    def test_item_not_in_list_less_than_min(self):
        self.assertFalse(binary_search([1, 2, 3], 0))

    def test_item_not_in_list_greater_than_max(self):
        self.assertFalse(binary_search([1, 2, 3], 4))

    def test_item_equal_to_min(self):
        self.assertTrue(binary_search([1, 1, 2, 3], 1))

    def test_item_equal_to_max(self):
        self.assertTrue(binary_search([1, 2, 3, 3], 3))
