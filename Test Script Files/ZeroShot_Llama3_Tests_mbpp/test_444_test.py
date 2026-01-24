import unittest
from mbpp_444_code import trim_tuple

class TestTrimTuple(unittest.TestCase):

    def test_trim_tuple(self):
        self.assertEqual(trim_tuple([(1, 2, 3, 4, 5), (6, 7, 8, 9, 10)], 1), "[(2, 3, 4), (7, 8, 9)]")
        self.assertEqual(trim_tuple([(1, 2, 3, 4, 5), (6, 7, 8, 9, 10)], 2), "[(1, 2, 3, 4), (6, 7, 8, 9)]")
        self.assertEqual(trim_tuple([(1, 2, 3, 4, 5), (6, 7, 8, 9, 10)], 3), "[(1, 2, 3, 4), (6, 7, 8, 9)]")
        self.assertEqual(trim_tuple([(1, 2, 3, 4, 5), (6, 7, 8, 9, 10)], 4), "[(1, 2, 3), (6, 7, 8)]")
        self.assertEqual(trim_tuple([(1, 2, 3, 4, 5), (6, 7, 8, 9, 10)], 5), "[(1, 2, 3, 4), ()]")
        self.assertEqual(trim_tuple([(1, 2, 3, 4, 5), (6, 7, 8, 9, 10)], 0), "[(1, 2, 3, 4), (6, 7, 8, 9)]")
        self.assertEqual(trim_tuple([(1, 2, 3, 4, 5), (6, 7, 8, 9, 10)], 6), "[(1, 2, 3, 4), ()]")
        self.assertEqual(trim_tuple([(1, 2, 3, 4, 5), (6, 7, 8, 9, 10)], 7), "[(1, 2, 3, 4), ()]")
        self.assertEqual(trim_tuple([(1, 2, 3, 4, 5), (6, 7, 8, 9, 10)], 8), "[(1, 2, 3, 4), ()]")
        self.assertEqual(trim_tuple([(1, 2, 3, 4, 5), (6, 7, 8, 9, 10)], 9), "[(1, 2, 3, 4), ()]")
        self.assertEqual(trim_tuple([(1, 2, 3, 4, 5), (6, 7, 8, 9, 10)], 10), "[(1, 2, 3, 4), ()]")

    def test_trim_tuple_empty(self):
        self.assertEqual(trim_tuple([], 1), "[]")
        self.assertEqual(trim_tuple([(1, 2, 3, 4, 5)], 1), "[(2, 3, 4)]")
        self.assertEqual(trim_tuple([(1, 2, 3, 4, 5)], 5), "[(1, 2, 3, 4)]")
        self.assertEqual(trim_tuple([(1, 2, 3, 4, 5)], 0), "[(1, 2, 3, 4)]")
        self.assertEqual(trim_tuple([(1, 2, 3, 4, 5)], 6), "[(1, 2, 3, 4)]")
