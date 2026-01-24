import unittest
from mbpp_280_code import sequential_search

class TestSequentialSearch(unittest.TestCase):

    def test_empty_list(self):
        self.assertFalse(sequential_search([], 1))

    def test_single_element_list(self):
        self.assertFalse(sequential_search([2], 1))
        self.assertEqual(sequential_search([1], 1), (True, 0))

    def test_found_in_middle(self):
        self.assertEqual(sequential_search([1, 2, 3, 4, 5], 3), (True, 2))

    def test_found_at_end(self):
        self.assertEqual(sequential_search([1, 2, 3, 4], 4), (True, 3))

    def test_not_found(self):
        self.assertFalse(sequential_search([1, 2, 3, 4], 5))
        self.assertFalse(sequential_search([1, 2, 3, 4], 0))

    def test_duplicate_values(self):
        self.assertEqual(sequential_search([1, 1, 2, 3, 4], 1), (True, 0 or 1))

    def test_invalid_input_list(self):
        self.assertRaises(TypeError, sequential_search, 1, 2)

    def test_invalid_input_item(self):
        self.assertRaises(TypeError, sequential_search, [1, 2, 3], 1.5)
