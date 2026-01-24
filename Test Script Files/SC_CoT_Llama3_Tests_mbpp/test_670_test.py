import unittest
from mbpp_670_code import decreasing_trend

class TestDecreasingTrend(unittest.TestCase):
    def test_decreasing_trend_true(self):
        self.assertTrue(decreasing_trend([1, 2, 3, 4, 5]))

    def test_decreasing_trend_false(self):
        self.assertFalse(decreasing_trend([5, 4, 3, 2, 1]))

    def test_decreasing_trend_sorted(self):
        self.assertTrue(decreasing_trend([1, 1, 1]))

    def test_decreasing_trend_empty(self):
        self.assertFalse(decreasing_trend([]))

    def test_decreasing_trend_single_element(self):
        self.assertFalse(decreasing_trend([1]))

    def test_decreasing_trend_duplicates(self):
        self.assertFalse(decreasing_trend([1, 2, 2, 3, 3, 3]))

    def test_decreasing_trend_non_integer(self):
        with self.assertRaises(TypeError):
            decreasing_trend(['a', 'b', 'c'])

    def test_decreasing_trend_mixed_types(self):
        with self.assertRaises(TypeError):
            decreasing_trend([1, 'a', 2, 3])
