import unittest
from mbpp_444_code import trim_tuple

class TestTrimTuple(unittest.TestCase):

    def test_trim_tuple(self):
        self.assertEqual(trim_tuple([(1, 2, 3, 4, 5), (6, 7, 8, 9, 10)], 2), '[(3, 4), (8, 9)]')
        self.assertEqual(trim_tuple([(1, 2, 3), (4, 5, 6)], 1), '[(2), (5)]')
        self.assertEqual(trim_tuple([(1, 2, 3, 4), (5, 6, 7, 8)], 0), '[(1, 2, 3, 4), (5, 6, 7, 8)]')
        self.assertEqual(trim_tuple([], 2), '[]')
        self.assertEqual(trim_tuple([(1, 2, 3, 4, 5)], 3), '[(2)]')
