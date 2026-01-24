import unittest
from mbpp_875_code import min_difference

class TestMinDifference(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(min_difference([1, 2]), 1)
        self.assertEqual(min_difference([-1, 1]), 2)
        self.assertEqual(min_difference([0, 0]), 0)

    def test_edge_and_boundary(self):
        self.assertEqual(min_difference([-1000000, -1]), 1000000)
        self.assertEqual(min_difference([1, 1000000]), 1000000)
        self.assertEqual(min_difference([-1, -1000000]), 2*1000000)
        self.assertEqual(min_difference([1000000, 1]), 2*1000000)
        self.assertEqual(min_difference([-1000000, -1000000]), 0)
        self.assertEqual(min_difference([1000000, 1000000]), 0)

    def test_complex(self):
        self.assertEqual(min_difference([-1, 0, 1]), 1)
        self.assertEqual(min_difference([1, 0, -1]), 1)
        self.assertEqual(min_difference([-1, 0, 1, 2]), 1)
        self.assertEqual(min_difference([1, 0, -1, -2]), 1)
        self.assertEqual(min_difference([-1, 0, 1, 2, 3]), 1)
        self.assertEqual(min_difference([1, 0, -1, -2, -3]), 1)
