import unittest
from mbpp_670_code import decreasing_trend

class TestDecreasingTrend(unittest.TestCase):
    def test_decreasing_trend_positive(self):
        self.assertTrue(decreasing_trend([5, 4, 3, 2, 1]))
        self.assertTrue(decreasing_trend([10, 9, 8, 7, 6]))

    def test_decreasing_trend_empty(self):
        self.assertFalse(decreasing_trend([]))

    def test_decreasing_trend_single_element(self):
        self.assertFalse(decreasing_trend([1]))

    def test_decreasing_trend_increasing(self):
        self.assertFalse(decreasing_trend([5, 4, 3, 2, 1, 2, 3]))
        self.assertFalse(decreasing_trend([10, 9, 8, 7, 6, 7, 8]))

    def test_decreasing_trend_duplicates(self):
        self.assertTrue(decreasing_trend([5, 5, 4, 3, 2, 1]))
        self.assertTrue(decreasing_trend([10, 10, 9, 8, 7, 6]))

    def test_decreasing_trend_reversed(self):
        self.assertTrue(decreasing_trend(reversed([5, 4, 3, 2, 1])))
        self.assertTrue(decreasing_trend(reversed([10, 9, 8, 7, 6])))
