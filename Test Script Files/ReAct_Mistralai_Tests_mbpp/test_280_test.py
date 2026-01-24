import unittest
from mbpp_280_code import sequential_search

class TestSequentialSearch(unittest.TestCase):

    def test_empty_list(self):
        self.assertFalse(sequential_search([], 1))

    def test_single_item_list(self):
        self.assertEqual(sequential_search([1], 1), (True, 0))
        self.assertFalse(sequential_search([1], 2))

    def test_multiple_items_list(self):
        self.assertEqual(sequential_search([1, 2, 3, 4], 3), (True, 2))
        self.assertFalse(sequential_search([1, 2, 3, 4], 5))

    def test_duplicate_items_list(self):
        self.assertEqual(sequential_search([1, 1, 2, 3], 1), (True, 0 or 1))

    def test_list_with_negative_numbers(self):
        self.assertEqual(sequential_search([-1, 0, 1], 0), (True, 1))

    def test_list_with_large_numbers(self):
        self.assertEqual(sequential_search([1000000, 2000000, 3000000], 3000000), (True, 2))

    def test_list_with_non_integer_items(self):
        self.assertRaises(TypeError, sequential_search, [1, 'two', 3], 'two')
