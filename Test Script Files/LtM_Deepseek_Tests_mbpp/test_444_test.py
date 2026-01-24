import unittest
from mbpp_444_code import trim_tuple

class TestTrimTuple(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(trim_tuple([(1, 2, 3, 4, 5)], 1), '[(2, 3, 4)]')
        self.assertEqual(trim_tuple([(1, 2, 3, 4, 5)], 2), '[(3, 4)]')
        self.assertEqual(trim_tuple([(1, 2, 3, 4, 5)], 0), '[(1, 2, 3, 4, 5)]')

    def test_edge_conditions(self):
        self.assertEqual(trim_tuple([], 1), '[]')
        self.assertEqual(trim_tuple([(1, 2)], 1), '[(1, 2)]')
        self.assertEqual(trim_tuple([(1, 2, 3, 4, 5)], 5), '[]')
        self.assertEqual(trim_tuple([(1, 2, 3, 4, 5)], -1), '[(1, 2, 3, 4, 5)]')

    def test_complex_cases(self):
        self.assertEqual(trim_tuple([(1, 2, 3, 4, 5), (6, 7, 8, 9, 10)], 2), '[(3, 4), (8, 9)]')
        self.assertEqual(trim_tuple([(1, 2, 3, 4, 5), (6, 7, 8, 9, 10)], 0), '[(1, 2, 3, 4, 5), (6, 7, 8, 9, 10)]')
