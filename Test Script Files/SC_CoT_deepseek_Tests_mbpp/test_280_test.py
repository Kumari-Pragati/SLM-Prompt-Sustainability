import unittest
from mbpp_280_code import sequential_search

class TestSequentialSearch(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(sequential_search([1, 2, 3, 4, 5], 3))

    def test_edge_case_item_at_start(self):
        self.assertTrue(sequential_search([3, 2, 1], 3))

    def test_edge_case_item_at_end(self):
        self.assertTrue(sequential_search([1, 2, 3], 3))

    def test_edge_case_item_not_in_list(self):
        self.assertFalse(sequential_search([1, 2, 3], 4))

    def test_edge_case_empty_list(self):
        self.assertFalse(sequential_search([], 1))

    def test_edge_case_single_item_in_list(self):
        self.assertTrue(sequential_search([1], 1))

    def test_edge_case_duplicate_items(self):
        self.assertTrue(sequential_search([1, 2, 2, 3], 2))

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            sequential_search("12345", 1)
