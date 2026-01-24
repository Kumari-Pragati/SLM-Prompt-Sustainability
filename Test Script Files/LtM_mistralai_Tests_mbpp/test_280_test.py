import unittest
from mbpp_280_code import sequential_search

class TestSequentialSearch(unittest.TestCase):

    def test_simple_search(self):
        self.assertTrue(sequential_search([1, 2, 3, 4, 5], 3))
        self.assertTrue(sequential_search(['a', 'b', 'c', 'd', 'e'], 'c'))
        self.assertTrue(sequential_search([0, 1, 2, 3, 4], 3))

    def test_edge_cases(self):
        self.assertFalse(sequential_search([], 1))
        self.assertFalse(sequential_search([1], 2))
        self.assertFalse(sequential_search([1, 2], 3))
        self.assertFalse(sequential_search([1, 2, 3], 4))
        self.assertFalse(sequential_search([1, 2, 3], 0))
        self.assertFalse(sequential_search(['a', 'b', 'c'], 'd'))
        self.assertFalse(sequential_search(['a', 'b', 'c'], 'z'))

    def test_boundary_conditions(self):
        self.assertTrue(sequential_search([0, 1, 2, 3, 4], 0))
        self.assertTrue(sequential_search(['a', 'b', 'c', 'd', 'e'], 'a'))
        self.assertTrue(sequential_search(['z', 'a', 'b', 'c', 'd'], 'z'))

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, sequential_search, [1, 2, 3], 1.5)
        self.assertRaises(TypeError, sequential_search, ['a', 'b', 'c'], 1)
