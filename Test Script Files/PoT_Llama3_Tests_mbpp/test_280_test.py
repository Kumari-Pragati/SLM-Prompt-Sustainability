import unittest
from mbpp_280_code import sequential_search

class TestSequentialSearch(unittest.TestCase):

    def test_found_at_first_position(self):
        self.assertTrue(sequential_search([1, 2, 3, 4, 5], 1)[0])

    def test_found_at_last_position(self):
        self.assertTrue(sequential_search([1, 2, 3, 4, 5], 5)[0])

    def test_found_in_middle_position(self):
        self.assertTrue(sequential_search([1, 2, 3, 4, 5], 3)[0])

    def test_not_found(self):
        self.assertFalse(sequential_search([1, 2, 3, 4, 5], 6)[0])

    def test_found_at_first_position_with_duplicates(self):
        self.assertTrue(sequential_search([1, 1, 2, 3, 4, 5], 1)[0])

    def test_found_at_last_position_with_duplicates(self):
        self.assertTrue(sequential_search([1, 1, 2, 3, 4, 5], 5)[0])

    def test_found_in_middle_position_with_duplicates(self):
        self.assertTrue(sequential_search([1, 1, 2, 3, 4, 5], 3)[0])

    def test_not_found_with_duplicates(self):
        self.assertFalse(sequential_search([1, 1, 2, 3, 4, 5], 6)[0])

    def test_empty_list(self):
        self.assertFalse(sequential_search([], 1)[0])

    def test_single_element_list(self):
        self.assertTrue(sequential_search([1], 1)[0])

    def test_list_with_one_occurrence(self):
        self.assertTrue(sequential_search([1, 2, 3, 4, 5], 2)[0])

    def test_list_with_no_occurrences(self):
        self.assertFalse(sequential_search([1, 2, 3, 4, 5], 6)[0])
