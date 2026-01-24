import unittest
from mbpp_680_code import increasing_trend

class TestIncreasingTrend(unittest.TestCase):

    def test_typical_cases(self):
        self.assertTrue(increasing_trend([1, 2, 3, 4, 5]))
        self.assertTrue(increasing_trend([1, 1, 1, 1, 1]))
        self.assertFalse(increasing_trend([5, 4, 3, 2, 1]))
        self.assertFalse(increasing_trend([1, 2, 1, 4, 5]))

    def test_edge_cases(self):
        self.assertTrue(increasing_trend([1]))
        self.assertFalse(increasing_trend([]))

    def test_boundary_cases(self):
        self.assertTrue(increasing_trend(list(range(1, 10001))))
        self.assertFalse(increasing_trend(list(range(10000, 0, -1))))

    def test_corner_cases(self):
        self.assertTrue(increasing_trend([1, 2, 3, 2, 1]))
        self.assertFalse(increasing_trend([1, 2, 3, 2, 3]))
