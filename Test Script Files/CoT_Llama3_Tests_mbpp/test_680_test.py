import unittest
from mbpp_680_code import increasing_trend

class TestIncreasingTrend(unittest.TestCase):
    def test_increasing_trend(self):
        self.assertTrue(increasing_trend([1, 2, 3, 4, 5]))
        self.assertTrue(increasing_trend([5, 4, 3, 2, 1]))
        self.assertFalse(increasing_trend([1, 1, 1, 1, 1]))
        self.assertFalse(increasing_trend([5, 4, 3, 2, 1, 5]))
        self.assertFalse(increasing_trend([1, 2, 3, 4, 5, 6, 5]))
        self.assertFalse(increasing_trend([1, 2, 3, 4, 5, 6, 7, 6]))
        self.assertFalse(increasing_trend([1, 2, 3, 4, 5, 6, 7, 8, 7]))
        self.assertFalse(increasing_trend([1, 2, 3, 4, 5, 6, 7, 8, 9, 8]))
        self.assertFalse(increasing_trend([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9]))
        self.assertFalse(increasing_trend([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 10]))
