import unittest
from mbpp_223_code import binary_search

class TestBinarySearch(unittest.TestCase):

    def test_normal(self):
        self.assertEqual(binary_search([1, 2, 3, 4, 5], 0, 4, 3), 2)
        self.assertEqual(binary_search([10, 10, 12, 15, 20], 0, 4, 10), 0)
        self.assertEqual(binary_search([-5, -3, -1, 0, 1, 3, 5], 0, 6, 0), 3)

    def test_edge_cases(self):
        self.assertEqual(binary_search([], 0, 0, 1), -1)
        self.assertEqual(binary_search([1], 0, 0, 1), 0)
        self.assertEqual(binary_search([1, 1], 0, 1, 2), -1)
        self.assertEqual(binary_search([1, 1], 0, 1, 1), 0)
        self.assertEqual(binary_search([1, 2, 3, 4, 5], 0, 5, 6), -1)
        self.assertEqual(binary_search([1, 2, 3, 4, 5], 5, 5, 5), 4)
        self.assertEqual(binary_search([1, 2, 3, 4, 5], 5, 5, 6), -1)

    def test_invalid_inputs(self):
        self.assertEqual(binary_search([1, 2, 3, 4, 5], -1, 4, 3), -1)
        self.assertEqual(binary_search([1, 2, 3, 4, 5], 0, -1, 3), -1)
        self.assertEqual(binary_search([1, 2, 3, 4, 5], 0, 4, -1), -1)
        self.assertEqual(binary_search([1, 2, 3, 4, 5], 0, 4, 6), -1)
