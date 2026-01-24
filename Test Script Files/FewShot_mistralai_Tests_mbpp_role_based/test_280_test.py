import unittest
from mbpp_280_code import sequential_search

class TestSequentialSearch(unittest.TestCase):
    def test_found_in_list(self):
        self.assertTrue(sequential_search([1, 2, 3, 4, 5], 3))

    def test_not_found_in_list(self):
        self.assertFalse(sequential_search([1, 2, 3, 4, 5], 6))

    def test_empty_list(self):
        self.assertFalse(sequential_search([]))

    def test_single_element_list(self):
        self.assertFalse(sequential_search([1], 2))

    def test_item_not_in_list(self):
        self.assertFalse(sequential_search([1, 2, 3], 4))

    def test_item_at_beginning_of_list(self):
        self.assertTrue(sequential_search([1], 1))

    def test_item_at_end_of_list(self):
        self.assertTrue(sequential_search([1, 2, 3], 3))
