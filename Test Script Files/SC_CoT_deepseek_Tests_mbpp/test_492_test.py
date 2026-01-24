import unittest
from mbpp_492_code import binary_search

class TestBinarySearch(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9], 5))

    def test_edge_case_first_element(self):
        self.assertTrue(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9], 1))

    def test_edge_case_last_element(self):
        self.assertTrue(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9], 9))

    def test_edge_case_single_element(self):
        self.assertTrue(binary_search([5], 5))

    def test_edge_case_empty_list(self):
        self.assertFalse(binary_search([], 5))

    def test_corner_case_not_found(self):
        self.assertFalse(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9], 10))

    def test_corner_case_duplicates(self):
        self.assertTrue(binary_search([1, 2, 2, 3, 4, 5, 6, 7, 8, 9], 2))

    def test_invalid_input_none(self):
        with self.assertRaises(TypeError):
            binary_search(None, 5)

    def test_invalid_input_non_list(self):
        with self.assertRaises(TypeError):
            binary_search("not a list", 5)

    def test_invalid_input_non_integer_in_list(self):
        with self.assertRaises(TypeError):
            binary_search([1, "not an integer", 3], 5)
