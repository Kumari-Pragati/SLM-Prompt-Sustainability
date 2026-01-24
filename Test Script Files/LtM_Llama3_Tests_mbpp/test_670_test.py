import unittest
from mbpp_670_code import decreasing_trend

class TestDecreasingTrend(unittest.TestCase):
    def test_empty_input(self):
        self.assertFalse(decreasing_trend([]))

    def test_single_element_input(self):
        self.assertTrue(decreasing_trend([1]))

    def test_decreasing_trend_input(self):
        self.assertTrue(decreasing_trend([5, 4, 3, 2, 1]))

    def test_increasing_trend_input(self):
        self.assertFalse(decreasing_trend([1, 2, 3, 4, 5]))

    def test_unsorted_input(self):
        self.assertFalse(decreasing_trend([3, 1, 2, 4, 5]))

    def test_duplicates_input(self):
        self.assertFalse(decreasing_trend([5, 4, 3, 3, 2, 1]))

    def test_empty_and_single_element_input(self):
        self.assertFalse(decreasing_trend([1,]))

    def test_empty_and_decreasing_trend_input(self):
        self.assertFalse(decreasing_trend([5, 4, 3, 2, 1,]))
