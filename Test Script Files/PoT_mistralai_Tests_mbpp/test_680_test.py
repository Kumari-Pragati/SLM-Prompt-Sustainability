import unittest
from mbpp_680_code import increasing_trend

class TestIncreasingTrend(unittest.TestCase):
    def test_typical_case(self):
        self.assertTrue(increasing_trend([1, 2, 3, 4, 5]))
        self.assertTrue(increasing_trend([-1, -2, -3, -4, -5]))
        self.assertTrue(increasing_trend([0, 1, 2, 3, 4]))

    def test_edge_case(self):
        self.assertFalse(increasing_trend([1, 2, 3, 4, 5, 6]))
        self.assertFalse(increasing_trend([1, 2, 3, 4, 5, 4]))
        self.assertFalse(increasing_trend([1, 2, 3, 4, 5, 3]))
        self.assertFalse(increasing_trend([1, 2, 3, 4, 5, 2]))
        self.assertFalse(increasing_trend([1, 2, 3, 4, 5, 1]))

    def test_corner_case(self):
        self.assertFalse(increasing_trend([]))
        self.assertFalse(increasing_trend([1]))
        self.assertTrue(increasing_trend([1, 1]))
