import unittest
from mbpp_492_code import binary_search

class TestBinarySearch(unittest.TestCase):

    def test_item_present(self):
        self.assertTrue(binary_search([1, 2, 3, 4, 5], 4))

    def test_item_absent(self):
        self.assertFalse(binary_search([1, 2, 3, 4, 5], 6))

    def test_empty_list(self):
        self.assertFalse(binary_search([], 4))

    def test_single_item_present(self):
        self.assertTrue(binary_search([4], 4))

    def test_single_item_absent(self):
        self.assertFalse(binary_search([4], 6))

    def test_duplicate_items(self):
        self.assertTrue(binary_search([1, 2, 3, 4, 4, 5], 4))

    def test_negative_numbers(self):
        self.assertTrue(binary_search([-5, -4, -3, -2, -1], -2))

    def test_non_sorted_list(self):
        with self.assertRaises(Exception):
            binary_search([3, 1, 4, 1, 5, 9], 4)
