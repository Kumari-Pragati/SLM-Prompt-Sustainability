import unittest
from mbpp_492_code import binary_search

class TestBinarySearch(unittest.TestCase):

    def test_simple(self):
        self.assertTrue(binary_search([1, 2, 3, 4, 5], 3))
        self.assertFalse(binary_search([1, 2, 3, 4, 5], 6))

    def test_edge_and_boundary(self):
        self.assertTrue(binary_search([], 0))
        self.assertFalse(binary_search([1], 0))
        self.assertTrue(binary_search([0], 0))
        self.assertFalse(binary_search([1, 2, 3], 0))
        self.assertFalse(binary_search([1, 2, 3], 4))
        self.assertTrue(binary_search([1, 2, 3], 3))
        self.assertTrue(binary_search([1, 2, 3], 2))
        self.assertTrue(binary_search([1, 2, 3], 1))

    def test_complex(self):
        self.assertTrue(binary_search([1, 3, 5, 7, 9], 5))
        self.assertFalse(binary_search([1, 3, 5, 7, 9], 0))
        self.assertFalse(binary_search([1, 3, 5, 7, 9], 10))
        self.assertTrue(binary_search([-1, -3, -5, -7, -9], -5))
        self.assertFalse(binary_search([-1, -3, -5, -7, -9], -10))
