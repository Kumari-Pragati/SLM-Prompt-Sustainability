import unittest
from mbpp_670_code import decreasing_trend

class TestDecreasingTrend(unittest.TestCase):
    def test_decreasing_trend_positive_numbers(self):
        self.assertTrue(decreasing_trend([5, 4, 3, 2, 1]))

    def test_decreasing_trend_zero(self):
        self.assertTrue(decreasing_trend([0, 0]))

    def test_decreasing_trend_increasing_numbers(self):
        self.assertFalse(decreasing_trend([1, 2, 3, 4, 5]))

    def test_decreasing_trend_duplicates(self):
        self.assertTrue(decreasing_trend([1, 1, 0]))

    def test_decreasing_trend_empty_list(self):
        self.assertIsNone(decreasing_trend([]))

    def test_decreasing_trend_single_element(self):
        self.assertTrue(decreasing_trend([0]))

    def test_decreasing_trend_negative_numbers(self):
        self.assertTrue(decreasing_trend([-5, -4, -3, -2, -1]))
