import unittest
from mbpp_670_code import decreasing_trend

class TestDecreasingTrend(unittest.TestCase):

    def test_empty_list(self):
        self.assertTrue(decreasing_trend([]))

    def test_single_element(self):
        self.assertTrue(decreasing_trend([1]))

    def test_increasing_trend(self):
        self.assertFalse(decreasing_trend([1, 2, 3]))

    def test_decreasing_trend(self):
        self.assertTrue(decreasing_trend([5, 4, 3]))

    def test_mixed_trend(self):
        self.assertFalse(decreasing_trend([5, 4, 3, 2, 1]))
