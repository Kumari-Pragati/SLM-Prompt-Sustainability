import unittest
from mbpp_769_code import Diff

class TestDiff(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(Diff([1, 2, 3], [2, 3, 4]), [[1], [4]])
        self.assertEqual(Diff(['a', 'b', 'c'], ['b', 'c', 'd']), [['a'], ['d']])

    def test_edge_cases(self):
        self.assertEqual(Diff([], [1, 2, 3]), [])
        self.assertEqual(Diff([1, 2, 3], []), [1, 2, 3])
        self.assertEqual(Diff([], []), [])

    def test_corner_cases(self):
        self.assertEqual(Diff([1], [1]), [])
        self.assertEqual(Diff([1, 2, 3], [1, 2, 3]), [])
