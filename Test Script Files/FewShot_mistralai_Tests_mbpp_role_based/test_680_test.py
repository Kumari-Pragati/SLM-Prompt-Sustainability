import unittest
from mbpp_680_code import increasing_trend

class TestIncreasingTrend(unittest.TestCase):
    def test_increasing_trend_positive(self):
        self.assertTrue(increasing_trend([1, 2, 3, 4, 5]))

    def test_increasing_trend_zero(self):
        self.assertTrue(increasing_trend([0, 1, 2, 3, 4]))

    def test_increasing_trend_decreasing(self):
        self.assertFalse(increasing_trend([5, 4, 3, 2, 1]))

    def test_increasing_trend_duplicates(self):
        self.assertTrue(increasing_trend([1, 1, 2, 3, 4]))

    def test_increasing_trend_empty(self):
        self.assertTrue(increasing_trend([]))

    def test_increasing_trend_single_element(self):
        self.assertTrue(increasing_trend([1]))

    def test_increasing_trend_reverse_order(self):
        self.assertFalse(increasing_trend([4, 3, 2, 1]))

    def test_increasing_trend_negative(self):
        self.assertTrue(increasing_trend([-1, -2, -3, -4, -5]))
