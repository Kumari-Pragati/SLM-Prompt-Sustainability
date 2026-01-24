import unittest
from mbpp_280_code import sequential_search

class TestSequentialSearch(unittest.TestCase):
    def test_found_at_first_position(self):
        self.assertTrue(sequential_search([1, 2, 3, 4, 5], 1), (1, 0))

    def test_found_at_last_position(self):
        self.assertTrue(sequential_search([1, 2, 3, 4, 5], 5), (5, 4))

    def test_found_in_middle(self):
        self.assertTrue(sequential_search([1, 2, 3, 4, 5], 3), (3, 2))

    def test_not_found(self):
        self.assertFalse(sequential_search([1, 2, 3, 4, 5], 6), (-1,))

    def test_empty_list(self):
        self.assertFalse(sequential_search([], 1), (-1,))

    def test_single_element_list(self):
        self.assertTrue(sequential_search([1], 1), (1, 0))

    def test_item_not_in_list(self):
        self.assertFalse(sequential_search([1, 2, 3, 4, 5], 6), (-1,))

    def test_item_at_end_of_list(self):
        self.assertTrue(sequential_search([1, 2, 3, 4, 5], 5), (5, 4))
