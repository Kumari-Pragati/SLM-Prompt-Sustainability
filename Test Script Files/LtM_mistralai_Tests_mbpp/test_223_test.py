import unittest
from mbpp_223_code import binary_search

class TestBinarySearch(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(binary_search([1, 2, 3, 4], 0, 3, 2), 1)
        self.assertEqual(binary_search([1, 2, 3, 4], 1, 3, 2), 1)
        self.assertEqual(binary_search([1, 2, 3, 4], 2, 3, 2), 2)
        self.assertEqual(binary_search([1, 2, 3, 4], 3, 3, 4), 3)

    def test_edge_and_boundary(self):
        self.assertEqual(binary_search([], 0, 0, 1), -1)
        self.assertEqual(binary_search([1], 0, 0, 1), 0)
        self.assertEqual(binary_search([1], 0, 1, 1), 0)
        self.assertEqual(binary_search([1], 0, 1, 2), -1)
        self.assertEqual(binary_search([1, 1], 0, 1, 1), 0)
        self.assertEqual(binary_search([1, 1], 0, 1, 2), -1)
        self.assertEqual(binary_search([1, 2, 3, 4], 0, 3, 5), -1)
        self.assertEqual(binary_search([1, 2, 3, 4], 4, 3, 4), 3)
        self.assertEqual(binary_search([1, 2, 3, 4], 4, 3, 5), -1)

    def test_complex(self):
        self.assertEqual(binary_search([1, 1, 2, 2, 3, 4], 0, 5, 1), 0)
        self.assertEqual(binary_search([1, 1, 2, 2, 3, 4], 1, 5, 1), 1)
        self.assertEqual(binary_search([1, 1, 2, 2, 3, 4], 2, 5, 2), 2)
        self.assertEqual(binary_search([1, 1, 2, 2, 3, 4], 3, 5, 3), 4)
        self.assertEqual(binary_search([1, 1, 2, 2, 3, 4], 4, 5, 4), 5)
