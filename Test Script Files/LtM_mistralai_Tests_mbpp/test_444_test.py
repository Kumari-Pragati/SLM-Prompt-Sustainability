import unittest
from mbpp_444_code import trim_tuple

class TestTrimTuple(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(trim_tuple([(1, 2, 3, 4, 5), (6, 7, 8, 9, 10)], 2), '[(3, 4), (8, 9)]')

    def test_edge_input(self):
        self.assertEqual(trim_tuple([(1, 2, 3), (4, 5, 6)], 0), '[(3), (6)]')
        self.assertEqual(trim_tuple([(1, 2, 3), (4, 5, 6)], 3), '[(1, 2), (4, 5)]')

    def test_boundary_input(self):
        self.assertEqual(trim_tuple([(1, 2, 3)], 1), '[(2, 3)]')
        self.assertEqual(trim_tuple([(1, 2, 3)], 2), '[(1), ]')

    def test_empty_input(self):
        self.assertEqual(trim_tuple([], 2), '[]')
