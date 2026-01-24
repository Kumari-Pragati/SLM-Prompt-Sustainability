import unittest
from mbpp_280_code import sequential_search

class TestSequentialSearch(unittest.TestCase):

    def test_simple_search(self):
        self.assertTrue(sequential_search([1, 2, 3, 4, 5], 3))
        self.assertFalse(sequential_search([1, 2, 3, 4, 5], 6))

    def test_empty_list(self):
        self.assertFalse(sequential_search([], 1))

    def test_single_element_list(self):
        self.assertTrue(sequential_search([5], 5))
        self.assertFalse(sequential_search([5], 6))

    def test_search_at_beginning(self):
        self.assertTrue(sequential_search([5, 6, 7, 8, 9], 5))

    def test_search_at_end(self):
        self.assertTrue(sequential_search([1, 2, 3, 4, 5], 5))

    def test_search_in_middle(self):
        self.assertTrue(sequential_search([1, 2, 3, 4, 5], 3))

    def test_search_not_present(self):
        self.assertFalse(sequential_search([1, 2, 3, 4, 5], 6))
