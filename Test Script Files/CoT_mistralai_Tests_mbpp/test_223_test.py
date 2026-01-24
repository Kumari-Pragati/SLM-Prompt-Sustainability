import unittest
from mbpp_223_code import binary_search

class TestBinarySearch(unittest.TestCase):
    def test_binary_search_found(self):
        self.assertEqual(binary_search([1, 2, 3, 4, 5], 0, 4, 3), 2)
        self.assertEqual(binary_search([10, 15, 20, 25, 30], 2, 4, 20), 3)

    def test_binary_search_not_found(self):
        self.assertEqual(binary_search([1, 2, 3, 4, 5], 0, 4, 6), -1)
        self.assertEqual(binary_search([10, 15, 20, 25, 30], 7, 4, 20), -1)

    def test_binary_search_empty_list(self):
        self.assertEqual(binary_search([], 0, 0, 3), -1)

    def test_binary_search_single_element(self):
        self.assertEqual(binary_search([3], 0, 0, 3), 0)

    def test_binary_search_duplicate_element(self):
        self.assertEqual(binary_search([3, 3], 0, 1, 3), 1)

    def test_binary_search_edge_case(self):
        self.assertEqual(binary_search([1, 1, 1, 2, 2, 2, 3], 0, 6, 1), 0)
        self.assertEqual(binary_search([1, 1, 1, 2, 2, 2, 3], 0, 6, 3), 5)
