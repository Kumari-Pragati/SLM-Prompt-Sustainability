import unittest
from mbpp_223_code import binary_search

class TestBinarySearch(unittest.TestCase):
    def test_typical_cases(self):
        self.assertEqual(binary_search([1, 2, 3, 4, 5], 0, 4, 3), 2)
        self.assertEqual(binary_search([10, 15, 1, 3, 8, 16, 20], 0, 6, 15), 4)
        self.assertEqual(binary_search([-5, -3, -2, -1, 0, 1, 3, 10], 0, 7, 0), 0)

    def test_edge_and_boundary_cases(self):
        self.assertEqual(binary_search([], 0, 0, 5), -1)
        self.assertEqual(binary_search([1], 0, 0, 1), 0)
        self.assertEqual(binary_search([1, 2], 0, 1, 3), -1)
        self.assertEqual(binary_search([1, 2], 0, 1, 2), 0)
        self.assertEqual(binary_search([1, 2], 1, 1, 2), 1)
        self.assertEqual(binary_search([1, 2], 0, 1, 0), -1)

        self.assertEqual(binary_search([1, 2, 3], 0, 2, 4), -1)
        self.assertEqual(binary_search([1, 2, 3], 2, 2, 1), -1)
        self.assertEqual(binary_search([1, 2, 3], 0, 2, 2), 1)
        self.assertEqual(binary_search([1, 2, 3], 1, 2, 3), 2)
        self.assertEqual(binary_search([1, 2, 3], 2, 2, 2), 2)

    def test_invalid_inputs(self):
        self.assertEqual(binary_search([1, 2, 3], -1, 4, 5), -1)
        self.assertEqual(binary_search([1, 2, 3], 5, 4, 5), -1)
        self.assertEqual(binary_search([1, 2, 3], 0, -1, 5), -1)
        self.assertEqual(binary_search([1, 2, 3], 0, 4, -1), -1)
