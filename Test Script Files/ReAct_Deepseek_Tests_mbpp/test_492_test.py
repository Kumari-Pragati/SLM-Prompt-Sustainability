import unittest
from mbpp_492_code import binary_search

class TestBinarySearch(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(binary_search([1, 2, 3, 4, 5], 4))

    def test_item_not_in_list(self):
        self.assertFalse(binary_search([1, 2, 3, 4, 5], 6))

    def test_empty_list(self):
        self.assertFalse(binary_search([], 4))

    def test_single_item_list(self):
        self.assertTrue(binary_search([4], 4))
        self.assertFalse(binary_search([4], 3))

    def test_duplicate_items(self):
        self.assertTrue(binary_search([1, 2, 3, 3, 5], 3))

    def test_negative_numbers(self):
        self.assertTrue(binary_search([-5, -3, -1, 0, 2], -1))
        self.assertFalse(binary_search([-5, -3, -1, 0, 2], -6))

    def test_large_numbers(self):
        self.assertTrue(binary_search(list(range(1, 10001)), 5000))
        self.assertFalse(binary_search(list(range(1, 10001)), 10001))
