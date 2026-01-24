import unittest
from mbpp_680_code import increasing_trend

class TestIncreasingTrend(unittest.TestCase):

    def test_increasing_trend(self):
        self.assertTrue(increasing_trend([1, 2, 3, 4, 5]))
        self.assertTrue(increasing_trend([1, 2, 3, 4, 5, 6]))
        self.assertTrue(increasing_trend([1, 2, 3, 4, 5, 6, 7]))
        self.assertTrue(increasing_trend([1, 2, 3, 4, 5, 6, 7, 8]))
        self.assertTrue(increasing_trend([1, 2, 3, 4, 5, 6, 7, 8, 9]))
        self.assertFalse(increasing_trend([1, 3, 2, 4, 5]))
        self.assertFalse(increasing_trend([1, 2, 3, 5, 4]))
        self.assertFalse(increasing_trend([1, 2, 3, 4, 6]))
        self.assertFalse(increasing_trend([1, 2, 3, 4, 5, 7]))
        self.assertFalse(increasing_trend([1, 2, 3, 4, 5, 6, 8]))
        self.assertFalse(increasing_trend([1, 2, 3, 4, 5, 6, 7, 9]))
        self.assertFalse(increasing_trend([1, 2, 3, 4, 5, 6, 7, 8, 10]))

    def test_edge_cases(self):
        self.assertTrue(increasing_trend([]))
        self.assertTrue(increasing_trend([1]))
        self.assertTrue(increasing_trend([1, 1]))
        self.assertFalse(increasing_trend([1, 2, 1]))
        self.assertFalse(increasing_trend([1, 2, 3, 1]))
