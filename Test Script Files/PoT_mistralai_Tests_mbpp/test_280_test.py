import unittest
from mbpp_280_code import sequential_search

class TestSequentialSearch(unittest.TestCase):
    def test_typical_case(self):
        self.assertTrue(sequential_search([1, 2, 3, 4, 5], 3))
        self.assertTrue(sequential_search(['a', 'b', 'c', 'd', 'e'], 'c'))
        self.assertTrue(sequential_search([0, 1, 2, 3, 4], 3))

    def test_edge_case_empty_list(self):
        self.assertFalse(sequential_search([], 1))

    def test_edge_case_single_item(self):
        self.assertTrue(sequential_search([1], 1))
        self.assertFalse(sequential_search([2], 1))

    def test_edge_case_item_not_found(self):
        self.assertFalse(sequential_search([1, 2, 3], 4))
        self.assertFalse(sequential_search(['a', 'b', 'c'], 'x'))
        self.assertFalse(sequential_search([0, 1, 2], 4))

    def test_corner_case_duplicate_item(self):
        self.assertTrue(sequential_search([1, 1, 2, 3], 1))
        self.assertTrue(sequential_search(['a', 'a', 'b', 'c'], 'a'))
        self.assertTrue(sequential_search([0, 0, 1, 2], 0))
