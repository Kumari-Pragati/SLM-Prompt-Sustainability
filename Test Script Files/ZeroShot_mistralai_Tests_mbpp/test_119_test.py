import unittest
from119_code import search

class TestSearchFunction(unittest.TestCase):

    def test_empty_list(self):
        self.assertIsNone(search([], 0))

    def test_single_element(self):
        self.assertEqual(search([1], 0), 1)

    def test_multiple_elements(self):
        self.assertEqual(search([1, 2, 3, 4, 5], 5), 0)

    def test_negative_numbers(self):
        self.assertEqual(search([-1, -2, -3, -4, -5], 5), 0)

    def test_duplicates(self):
        self.assertEqual(search([1, 1, 2, 3, 4, 5], 5), 0)

    def test_large_input(self):
        self.assertEqual(search([1000, 2000, 3000, 4000, 5000], 5000), 0)
