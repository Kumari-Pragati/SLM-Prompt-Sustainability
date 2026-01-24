import unittest
from mbpp_223_code import binary_search

class TestBinarySearch(unittest.TestCase):

    def test_binary_search_empty_list(self):
        self.assertEqual(binary_search([], 0, 0, 5), -1)

    def test_binary_search_single_element(self):
        self.assertEqual(binary_search([5], 0, 0, 5), 0)
        self.assertEqual(binary_search([5], 0, 0, 4), -1)

    def test_binary_search_middle_element(self):
        self.assertEqual(binary_search([1, 3, 5, 7], 0, 3, 5), 1)

    def test_binary_search_not_present(self):
        self.assertEqual(binary_search([1, 3, 5, 7], 0, 3, 2), -1)
        self.assertEqual(binary_search([1, 3, 5, 7], 0, 3, 9), -1)

    def test_binary_search_duplicate_middle(self):
        self.assertEqual(binary_search([1, 1, 3, 5, 7], 0, 4, 1), 2)

    def test_binary_search_duplicate_end(self):
        self.assertEqual(binary_search([1, 1, 3, 5, 5], 0, 4, 5), 3)

    def test_binary_search_duplicate_start(self):
        self.assertEqual(binary_search([5, 5, 3, 1], 0, 3, 5), 0)

    def test_binary_search_out_of_range(self):
        self.assertEqual(binary_search([1, 3, 5, 7], 4, 4, 5), -1)
        self.assertEqual(binary_search([1, 3, 5, 7], -1, 0, 5), -1)
