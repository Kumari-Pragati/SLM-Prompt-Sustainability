import unittest
from mbpp_769_code import Diff

class TestDiff(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(Diff([1, 2, 3], [2, 3, 4]), [1, 4])
        self.assertEqual(Diff([1, 1, 2], [2, 2, 3]), [1])
        self.assertEqual(Diff([], [1, 2, 3]), [1, 2, 3])
        self.assertEqual(Diff([1, 2, 3], []), [1, 2, 3])

    def test_edge_case(self):
        self.assertEqual(Diff([0], [1]), [0])
        self.assertEqual(Diff([1], [0]), [1])
        self.assertEqual(Diff([-1], [1]), [-1])
        self.assertEqual(Diff([1], [-1]), [1])

    def test_boundary_case(self):
        self.assertEqual(Diff([], []), [])
        self.assertEqual(Diff([1], []), [1])
        self.assertEqual(Diff([], [1]), [1])
