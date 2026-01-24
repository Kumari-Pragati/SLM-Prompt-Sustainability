import unittest
from mbpp_280_code import sequential_search

class TestSequentialSearch(unittest.TestCase):

    def test_normal_case(self):
        self.assertEqual(sequential_search([1, 2, 3, 4, 5], 3), (True, 2))
        self.assertEqual(sequential_search(["a", "b", "c", "d", "e"], "c"), (True, 2))
        self.assertEqual(sequential_search([10, 20, 30, 40, 50], 30), (True, 3))

    def test_edge_cases(self):
        self.assertEqual(sequential_search([], 1), (False, 0))
        self.assertEqual(sequential_search([1], 1), (True, 0))
        self.assertEqual(sequential_search([1, 2], 3), (False, 2))
        self.assertEqual(sequential_search([1, 2, 3], 4), (False, 3))
        self.assertEqual(sequential_search([1, 2, 3], 1), (True, 0))
        self.assertEqual(sequential_search(["a", "b", "c"], "z"), (False, 3))
        self.assertEqual(sequential_search(["a", "b", "c"], "a"), (True, 0))

    def test_boundary_cases(self):
        self.assertEqual(sequential_search([-1, 0, 1], 0), (True, 1))
        self.assertEqual(sequential_search([-1, 0, 1], -1), (True, 0))
        self.assertEqual(sequential_search([1e10, 2e10, 3e10], 3e10), (True, 2))
        self.assertEqual(sequential_search([1e10, 2e10, 3e10], 4e10), (False, 3))
