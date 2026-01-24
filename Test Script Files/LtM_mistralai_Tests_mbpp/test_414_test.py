import unittest
from mbpp_414_code import overlapping

class TestOverlapping(unittest.TestCase):

    def test_simple_overlap(self):
        self.assertEqual(overlapping([1, 2, 3], [3, 4, 5]), 1)
        self.assertEqual(overlapping([1, 1, 2], [1, 2, 3]), 1)
        self.assertEqual(overlapping([1, 2, 3], [1, 2, 4]), 0)

    def test_edge_cases(self):
        self.assertEqual(overlapping([], []), 0)
        self.assertEqual(overlapping([1], []), 0)
        self.assertEqual(overlapping([1], [1]), 1)
        self.assertEqual(overlapping([1, 1], [1, 1]), 1)
        self.assertEqual(overlapping([1, 2, 3], [3, 2, 1]), 1)
        self.assertEqual(overlapping([1, 2, 3], [3, 4, 5, 6]), 0)

    def test_boundary_cases(self):
        self.assertEqual(overlapping([1, 2, 3, 4], [4, 3, 2, 1]), 1)
        self.assertEqual(overlapping([1, 2, 3, 4], [4, 3, 2, 1, 0]), 1)
        self.assertEqual(overlapping([1, 2, 3, 4], [4, 3, 2, 1, 5]), 0)
        self.assertEqual(overlapping([1, 2, 3, 4], [4, 3, 2, 1, -1]), 0)
