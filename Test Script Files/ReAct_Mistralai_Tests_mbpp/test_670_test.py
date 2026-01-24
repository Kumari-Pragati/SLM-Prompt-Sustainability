import unittest
from mbpp_670_code import decreasing_trend

class TestDecreasingTrend(unittest.TestCase):

    def test_decreasing_trend_empty_list(self):
        self.assertFalse(decreasing_trend([]))

    def test_decreasing_trend_single_element(self):
        self.assertTrue(decreasing_trend([1]))
        self.assertFalse(decreasing_trend([2]))

    def test_decreasing_trend_increasing_list(self):
        self.assertFalse(decreasing_trend([1, 2, 3]))
        self.assertFalse(decreasing_trend([3, 2, 1]))

    def test_decreasing_trend_decreasing_list(self):
        self.assertTrue(decreasing_trend([3, 2, 1]))
        self.assertTrue(decreasing_trend([1, 2, 0]))

    def test_decreasing_trend_duplicates(self):
        self.assertTrue(decreasing_trend([1, 1, 0]))
        self.assertTrue(decreasing_trend([0, 0, 0]))

    def test_decreasing_trend_mixed_list(self):
        self.assertFalse(decreasing_trend([1, 2, 0, 1]))
        self.assertTrue(decreasing_trend([1, 2, 0, 2]))
