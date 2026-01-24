import unittest
from mbpp_119_code import search

class TestSearch(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(search([1, 2, 3, 4, 5], 5), 0)
        self.assertEqual(search([1, 1, 1, 1, 1], 5), 0)
        self.assertEqual(search([1, 2, 3, 4, 5, 6], 6), 0)

    def test_empty_list(self):
        self.assertIsNone(search([], 0))

    def test_single_element_list(self):
        self.assertEqual(search([1], 1), 0)

    def test_negative_number(self):
        self.assertRaises(ValueError, search, [-1, -2, -3], -1)

    def test_zero_length_input(self):
        self.assertRaises(ValueError, search, [1, 2, 3], 0)
