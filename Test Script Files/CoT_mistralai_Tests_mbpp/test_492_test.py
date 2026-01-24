import unittest
from492_code import binary_search

class TestBinarySearch(unittest.TestCase):
    def test_empty_list(self):
        self.assertFalse(binary_search([], 1))

    def test_single_item_list(self):
        self.assertFalse(binary_search([1], 2))
        self.assertTrue(binary_search([2], 2))

    def test_found_in_middle(self):
        self.assertTrue(binary_search([1, 2, 3, 4], 3))

    def test_found_at_beginning(self):
        self.assertTrue(binary_search([4, 5, 6], 4))

    def test_found_at_end(self):
        self.assertTrue(binary_search([1, 2, 3], 3))

    def test_not_found(self):
        self.assertFalse(binary_search([1, 2, 3], 4))

    def test_duplicates(self):
        self.assertTrue(binary_search([1, 1, 2, 3], 1))

    def test_negative_numbers(self):
        self.assertTrue(binary_search([-1, -2, -3], -1))

    def test_large_numbers(self):
        self.assertTrue(binary_search([1000000001, 1000000002, 1000000003], 1000000003))

    def test_invalid_input_list(self):
        with self.assertRaises(TypeError):
            binary_search('list', 1)

    def test_invalid_input_item(self):
        with self.assertRaises(TypeError):
            binary_search([1], 'item')
