import unittest
from mbpp_702_code import removals

class TestRemovals(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(removals([1, 2, 3, 4], 4, 1), 0)
        self.assertEqual(removals([1, 2, 3, 4], 4, 2), 1)
        self.assertEqual(removals([1, 2, 3, 4], 4, 3), 2)

    def test_edge_cases(self):
        self.assertEqual(removals([1, 2, 3], 3, 1), 2)
        self.assertEqual(removals([1, 2, 3], 3, 2), 1)
        self.assertEqual(removals([], 0, 1), 0)
        self.assertEqual(removals([1], 1, 1), 0)
        self.assertEqual(removals([1, 1], 2, 1), 1)

    def test_boundary_cases(self):
        self.assertEqual(removals([1, 2, 3, 4], 4, 0), 4)
        self.assertEqual(removals([1, 2, 3, 4], 4, 4), 0)

    def test_complex_cases(self):
        self.assertEqual(removals([1, 2, 2, 3, 4], 5, 1), 2)
        self.assertEqual(removals([1, 1, 2, 2, 3], 5, 1), 3)
        self.assertEqual(removals([1, 1, 2, 2, 3], 5, 2), 2)
