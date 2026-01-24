import unittest
from mbpp_670_code import decreasing_trend

class TestDecreasingTrend(unittest.TestCase):
    def test_decreasing_trend_positive_numbers(self):
        self.assertTrue(decreasing_trend([5, 4, 3, 2, 1]))

    def test_decreasing_trend_negative_numbers(self):
        self.assertTrue(decreasing_trend([-5, -4, -3, -2, -1]))

    def test_decreasing_trend_mixed_numbers(self):
        self.assertTrue(decreasing_trend([5, 4, -3, 2, 1]))

    def test_decreasing_trend_equal_numbers(self):
        self.assertFalse(decreasing_trend([5, 5, 5, 5, 5]))

    def test_decreasing_trend_empty_list(self):
        self.assertFalse(decreasing_trend([]))

    def test_decreasing_trend_single_element_list(self):
        self.assertFalse(decreasing_trend([5]))
