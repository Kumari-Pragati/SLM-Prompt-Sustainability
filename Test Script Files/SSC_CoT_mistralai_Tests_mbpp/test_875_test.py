import unittest
from mbpp_875_code import min_difference

class TestMinDifference(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(min_difference([1, 2, 3, 4, 5]), 1)
        self.assertEqual(min_difference([-1, 0, 1, 2, 3]), 0)
        self.assertEqual(min_difference([0, 1, 2, 3, 4]), 0)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(min_difference([0]), 0)
        self.assertEqual(min_difference([1]), 0)
        self.assertEqual(min_difference([-1]), 0)
        self.assertEqual(min_difference([-1, 0]), 1)
        self.assertEqual(min_difference([1, 2, 3]), 1)
        self.assertEqual(min_difference([-1, 0, 1]), 0)
        self.assertEqual(min_difference([-1, 0, 1, 2]), 1)
        self.assertEqual(min_difference([-1, 0, 1, 2, 3]), 0)
        self.assertEqual(min_difference([-1, 0, 1, 2, 3, 4]), 1)

    def test_invalid_input(self):
        self.assertRaises(TypeError, min_difference, [1, 'a'])
        self.assertRaises(TypeError, min_difference, ['a', 'b'])
        self.assertRaises(TypeError, min_difference, [1, 2, 3, 'a'])
