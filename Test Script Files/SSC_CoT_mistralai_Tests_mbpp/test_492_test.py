import unittest
from mbpp_492_code import binary_search

class TestBinarySearch(unittest.TestCase):

    def test_normal_case(self):
        self.assertTrue(binary_search([1, 2, 3, 4, 5], 3))
        self.assertTrue(binary_search([10, 20, 30, 40, 50], 30))
        self.assertTrue(binary_search(["apple", "banana", "cherry", "date"], "cherry"))

    def test_edge_cases(self):
        self.assertFalse(binary_search([], 1))
        self.assertFalse(binary_search([1], 2))
        self.assertFalse(binary_search([1, 2], 0))
        self.assertFalse(binary_search([1, 2], 3))
        self.assertFalse(binary_search([1, 2], 4))
        self.assertFalse(binary_search([1, 2], 5))
        self.assertFalse(binary_search([1, 2], 6))

    def test_boundary_cases(self):
        self.assertTrue(binary_search([1, 1], 1))
        self.assertTrue(binary_search([2, 2], 2))
        self.assertFalse(binary_search([1, 2], 2.5))
        self.assertTrue(binary_search(["a", "aa", "aaa"], "aa"))
        self.assertFalse(binary_search(["a", "aa", "aaa"], "aaaa"))

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, binary_search, [1, 2], 1.5)
        self.assertRaises(TypeError, binary_search, ["a", "b"], 1)
        self.assertRaises(ValueError, binary_search, [], None)
        self.assertRaises(ValueError, binary_search, [1], None)
