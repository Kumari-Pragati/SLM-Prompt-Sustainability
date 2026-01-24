import unittest
from mbpp_702_code import removals

class TestRemovals(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(removals([1, 3, 4, 9, 10, 11, 12, 17], 8, 2), 2)

    def test_edge_case(self):
        self.assertEqual(removals([1], 1, 0), 1)

    def test_boundary_case(self):
        self.assertEqual(removals([1, 2, 3, 4, 5], 5, 0), 1)
        self.assertEqual(removals([1, 2, 3, 4, 5], 5, 5), 1)

    def test_corner_case(self):
        self.assertEqual(removals([1, 2, 3, 4, 5], 5, 1), 1)
        self.assertEqual(removals([5, 4, 3, 2, 1], 5, 1), 1)
        self.assertEqual(removals([1, 2, 3, 4, 5], 5, 2), 1)
        self.assertEqual(removals([5, 4, 3, 2, 1], 5, 2), 1)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            removals("1, 2, 3, 4, 5", 5, 2)
        with self.assertRaises(ValueError):
            removals([1, 2, 3, 4, 5], -1, 2)
        with self.assertRaises(ValueError):
            removals([1, 2, 3, 4, 5], 5, -2)
