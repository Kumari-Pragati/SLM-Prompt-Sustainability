import unittest
from mbpp_444_code import trim_tuple

class TestTrimTuple(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(trim_tuple([(1, 2, 3, 4, 5), (6, 7, 8, 9, 10)], 2), '[(3, 4), (7, 8)]')
        self.assertEqual(trim_tuple([(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)], 1), '[(2), (4), (6), (8), (10)]')

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(trim_tuple([(1, 2, 3)], 0), '[(3)]')
        self.assertEqual(trim_tuple([(1, 2, 3)], 2), '[(1, 2)]')
        self.assertEqual(trim_tuple([(1, 2, 3)], 4), '[]')
        self.assertEqual(trim_tuple([(1, 2, 3)], 5), '[]')

    def test_negative_k(self):
        self.assertEqual(trim_tuple([(1, 2, 3)], -1), '[]')
        self.assertEqual(trim_tuple([(1, 2, 3)], -2), '[]')

    def test_invalid_input(self):
        self.assertRaises(TypeError, trim_tuple, [1, 2, 3], 'a')
        self.assertRaises(TypeError, trim_tuple, [(1,), (2, 3)], 0.5)
