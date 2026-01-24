import unittest
from mbpp_875_code import min_difference

class TestMinDifference(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(min_difference([(1, 2), (3, 4)]), 1)
    def test_empty(self):
        self.assertEqual(min_difference([]), None)
    def test_single(self):
        self.assertEqual(min_difference([(1, 1)]), 0)
    def test_edge(self):
        self.assertEqual(min_difference([(1, 2), (2, 3), (3, 4)]), 1)
    def test_max(self):
        self.assertEqual(min_difference([(1, 10), (2, 11), (3, 12)]), 1)
    def test_min(self):
        self.assertEqual(min_difference([(1, 0), (2, 1), (3, 2)]), 1)
    def test_multiple(self):
        self.assertEqual(min_difference([(1, 2), (2, 3), (3, 4), (4, 5)]), 1)
    def test_negative(self):
        self.assertEqual(min_difference([(-1, 0), (0, 1), (1, 2)]), 1)
