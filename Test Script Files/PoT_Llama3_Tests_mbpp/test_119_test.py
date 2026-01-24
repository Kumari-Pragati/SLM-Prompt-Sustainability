import unittest
from mbpp_119_code import search

class TestSearch(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(search([1, 2, 3, 4, 5], 5), 0)

    def test_edge_case_zero(self):
        self.assertEqual(search([0, 0, 0, 0, 0], 5), 0)

    def test_edge_case_single_element(self):
        self.assertEqual(search([1], 1), 1)

    def test_edge_case_all_same(self):
        self.assertEqual(search([1, 1, 1, 1, 1], 5), 0)

    def test_edge_case_all_diff(self):
        self.assertEqual(search([1, 2, 3, 4, 5], 5), 0)

    def test_edge_case_empty(self):
        with self.assertRaises(IndexError):
            search([], 0)

    def test_edge_case_negative(self):
        with self.assertRaises(IndexError):
            search([-1, -2, -3, -4, -5], 5)
