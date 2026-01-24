import unittest
from mbpp_702_code import removals

class TestRemovals(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(removals([1, 2, 3, 2, 1], 5, 1), 3)
        self.assertEqual(removals([4, 5, 6, 7, 8], 5, 2), 1)
        self.assertEqual(removals([-1, 0, 1, 2, 3], 5, 1), 4)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(removals([], 0, 1), 0)
        self.assertEqual(removals([1], 1, 1), 0)
        self.assertEqual(removals([1, 1], 2, 1), 1)
        self.assertEqual(removals([1, 2, 1], 3, 1), 2)
        self.assertEqual(removals([1, 2, 1], 3, 2), 2)
        self.assertEqual(removals([1, 2, 1], 3, 3), 0)

    def test_invalid_inputs(self):
        self.assertRaises(ValueError, removals, [], 0, 1)
        self.assertRaises(ValueError, removals, [1], -1, 1)
        self.assertRaises(ValueError, removals, [1], 0, -1)
