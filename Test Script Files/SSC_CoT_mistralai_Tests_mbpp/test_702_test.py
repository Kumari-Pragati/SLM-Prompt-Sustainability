import unittest
from mbpp_702_code import removals

class TestRemovals(unittest.TestCase):

    def test_typical_input(self):
        self.assertEqual(removals([3, 1, 2, 4, 5, 6], 6, 3), 1)
        self.assertEqual(removals([-5, -4, -3, -2, -1, 0], 6, 2), 1)
        self.assertEqual(removals([1, 2, 3, 4, 5], 5, 1), 0)

    def test_edge_cases(self):
        self.assertEqual(removals([], 0, 0), 0)
        self.assertEqual(removals([1], 1, 0), 0)
        self.assertEqual(removals([1, 2], 2, 1), 1)
        self.assertEqual(removals([1, 2, 3], 3, 2), 0)
        self.assertEqual(removals([1, 2, 3], 3, 3), 0)

    def test_boundary_conditions(self):
        self.assertEqual(removals([1, 2, 3], 3, 0), 0)
        self.assertEqual(removals([1, 2, 3], 3, 4), 0)

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, removals, [1, 2, 3], -1, 0)
        self.assertRaises(TypeError, removals, [1, 2, 3], 0, -1)
        self.assertRaises(TypeError, removals, [1, 2, 3], 0, "k")
