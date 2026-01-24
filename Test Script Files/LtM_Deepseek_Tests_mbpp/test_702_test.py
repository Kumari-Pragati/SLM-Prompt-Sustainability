import unittest
from mbpp_702_code import removals

class TestRemovals(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(removals([1, 2, 3, 4, 5], 5, 0), 0)
        self.assertEqual(removals([5, 10, 15, 20, 25], 5, 5), 1)
        self.assertEqual(removals([1, 2, 3, 4, 5], 5, 1), 1)

    def test_edge_conditions(self):
        self.assertEqual(removals([], 0, 1), 0)
        self.assertEqual(removals([1], 1, 0), 0)
        self.assertEqual(removals([1], 1, 1), 0)

    def test_boundary_conditions(self):
        self.assertEqual(removals([1, 2, 3, 4, 5], 5, 10), 0)
        self.assertEqual(removals([1, 2, 3, 4, 5], 5, 100), 1)
        self.assertEqual(removals([100, 200, 300, 400, 500], 5, 100), 1)

    def test_complex_cases(self):
        self.assertEqual(removals([1, 2, 3, 4, 5], 5, 2), 2)
        self.assertEqual(removals([5, 10, 15, 20, 25], 5, 10), 1)
        self.assertEqual(removals([1, 2, 3, 4, 5], 5, 3), 1)
