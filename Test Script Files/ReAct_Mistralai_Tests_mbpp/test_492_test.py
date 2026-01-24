import unittest
from mbpp_492_code import binary_search

class TestBinarySearch(unittest.TestCase):

    def test_empty_list(self):
        self.assertFalse(binary_search([], 1))

    def test_single_element_list(self):
        self.assertFalse(binary_search([2], 1))
        self.assertTrue(binary_search([1], 1))

    def test_middle_element(self):
        self.assertTrue(binary_search([1, 3, 5, 7], 5))

    def test_first_element(self):
        self.assertTrue(binary_search([1, 3, 5], 1))

    def test_last_element(self):
        self.assertTrue(binary_search([1, 3, 5], 5))

    def test_not_present(self):
        self.assertFalse(binary_search([1, 3, 5], 7))

    def test_duplicate_element(self):
        self.assertTrue(binary_search([1, 1, 3, 5], 1))

    def test_negative_numbers(self):
        self.assertTrue(binary_search([-2, -1, 0, 1, 2], -1))
        self.assertFalse(binary_search([-2, -1, 0, 1, 2], 3))

    def test_large_numbers(self):
        self.assertTrue(binary_search([1, 3, 5, 7, 9, 11, 13, 15], 11))

    def test_out_of_range_values(self):
        self.assertFalse(binary_search([1, 3, 5], 0))
        self.assertFalse(binary_search([1, 3, 5], 6))
