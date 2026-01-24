import unittest
from mbpp_414_code import overlapping

class TestOverlapping(unittest.TestCase):

    def test_no_overlap(self):
        self.assertEqual(overlapping([1, 2, 3], [4, 5, 6]), 0)

    def test_overlap(self):
        self.assertEqual(overlapping([1, 2, 3], [2, 4, 5]), 1)

    def test_overlap_reverse(self):
        self.assertEqual(overlapping([2, 4, 5], [1, 2, 3]), 1)

    def test_no_overlap_empty(self):
        self.assertEqual(overlapping([], [1, 2, 3]), 0)

    def test_overlap_empty(self):
        self.assertEqual(overlapping([1, 2, 3], []), 0)

    def test_overlap_same(self):
        self.assertEqual(overlapping([1, 2, 3], [1, 2, 3]), 1)

    def test_overlap_same_reverse(self):
        self.assertEqual(overlapping([1, 2, 3], [3, 2, 1]), 1)
