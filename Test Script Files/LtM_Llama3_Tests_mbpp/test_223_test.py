import unittest
from mbpp_223_code import binary_search

class TestBinarySearch(unittest.TestCase):
    def test_simple(self):
        self.assertTrue(binary_search([1, 2, 3, 4, 5], 5, 5))
        self.assertFalse(binary_search([1, 2, 3, 4, 5], 5, 6))

    def test_edge(self):
        self.assertFalse(binary_search([], 0, 0, 5))
        self.assertFalse(binary_search([5], 1, 1, 6))

    def test_edge2(self):
        self.assertTrue(binary_search([1, 2, 3, 4, 5], 5, 5))
        self.assertFalse(binary_search([1, 2, 3, 4, 5], 5, 6))

    def test_edge3(self):
        self.assertFalse(binary_search([1, 2, 3, 4, 5], 5, 6))

    def test_edge4(self):
        self.assertFalse(binary_search([1, 2, 3, 4, 5], 5, 6))

    def test_edge5(self):
        self.assertFalse(binary_search([1, 2, 3, 4, 5], 5, 6))

    def test_edge6(self):
        self.assertFalse(binary_search([1, 2, 3, 4, 5], 5, 6))

    def test_edge7(self):
        self.assertFalse(binary_search([1, 2, 3, 4, 5], 5, 6))

    def test_edge8(self):
        self.assertFalse(binary_search([1, 2, 3, 4, 5], 5, 6))

    def test_edge9(self):
        self.assertFalse(binary_search([1, 2, 3, 4, 5], 5, 6))

    def test_edge10(self):
        self.assertFalse(binary_search([1, 2, 3, 4, 5], 5, 6))
