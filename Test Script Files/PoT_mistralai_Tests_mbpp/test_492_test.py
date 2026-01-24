import unittest
from492_code import binary_search

class TestBinarySearch(unittest.TestCase):
    def test_typical_case(self):
        self.assertTrue(binary_search([1, 2, 3, 4, 5], 3))
        self.assertTrue(binary_search([10, 20, 30, 40, 50], 30))
        self.assertTrue(binary_search(["apple", "banana", "cherry", "date"], "banana"))

    def test_edge_case_empty_list(self):
        self.assertFalse(binary_search([], 1))

    def test_edge_case_single_element(self):
        self.assertTrue(binary_search([1], 1))
        self.assertFalse(binary_search([1], 2))

    def test_edge_case_first_element(self):
        self.assertTrue(binary_search([1, 2], 1))

    def test_edge_case_last_element(self):
        self.assertTrue(binary_search([1, 2], 2))

    def test_edge_case_not_present(self):
        self.assertFalse(binary_search([1, 2, 3], 4))
        self.assertFalse(binary_search(["apple", "banana", "cherry"], "orange"))

    def test_edge_case_negative_number(self):
        self.assertFalse(binary_search([-1, -2, -3], 0))

    def test_edge_case_floating_point(self):
        self.assertTrue(binary_search([1.1, 1.2, 1.3], 1.2))
        self.assertFalse(binary_search([1.1, 1.2, 1.3], 1.4))
