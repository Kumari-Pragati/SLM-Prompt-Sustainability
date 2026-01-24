import unittest
from mbpp_223_code import binary_search, is_majority

class TestBinarySearch(unittest.TestCase):
    def test_binary_search_empty_list(self):
        self.assertEqual(binary_search([], 0, 0, 5), -1)

    def test_binary_search_single_element(self):
        self.assertEqual(binary_search([5], 0, 0, 5), 0)

    def test_binary_search_not_found(self):
        self.assertEqual(binary_search([1, 2, 3, 4, 5], 0, 4, 6), -1)

    def test_binary_search_found_middle(self):
        self.assertEqual(binary_search([1, 2, 3, 4, 5], 0, 4, 3), 2)

    def test_binary_search_found_start(self):
        self.assertEqual(binary_search([5, 4, 3, 2, 1], 0, 4, 1), 0)

    def test_binary_search_found_end(self):
        self.assertEqual(binary_search([1, 2, 3, 4, 5], 0, 4, 5), 4)

class TestIsMajority(unittest.TestCase):
    def test_is_majority_less_than_half(self):
        self.assertFalse(is_majority([1, 1, 2, 3], 4, 1))

    def test_is_majority_equal_half(self):
        self.assertFalse(is_majority([1, 1, 2, 2, 3], 5, 2))

    def test_is_majority_more_than_half_single_element(self):
        self.assertTrue(is_majority([1, 1, 1, 1, 2], 5, 1))

    def test_is_majority_more_than_half_multiple_elements(self):
        self.assertTrue(is_majority([1, 1, 1, 2, 2], 5, 1))
