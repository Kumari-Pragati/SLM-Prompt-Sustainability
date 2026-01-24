import unittest
from mbpp_670_code import decreasing_trend

class TestDecreasingTrend(unittest.TestCase):

    def test_decreasing_trend_true(self):
        self.assertTrue(decreasing_trend([1, 2, 3, 4, 5]))

    def test_decreasing_trend_false(self):
        self.assertFalse(decreasing_trend([5, 4, 3, 2, 1]))

    def test_decreasing_trend_empty_list(self):
        self.assertFalse(decreasing_trend([]))

    def test_decreasing_trend_single_element(self):
        self.assertTrue(decreasing_trend([1]))

    def test_decreasing_trend_sorted_list(self):
        self.assertTrue(decreasing_trend([1, 1, 1, 1, 1]))

    def test_decreasing_trend_unsorted_list(self):
        self.assertFalse(decreasing_trend([2, 1, 3, 4, 5]))
