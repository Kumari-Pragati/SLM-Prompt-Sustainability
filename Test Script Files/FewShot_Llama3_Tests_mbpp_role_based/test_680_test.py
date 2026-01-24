import unittest
from mbpp_680_code import increasing_trend

class TestIncreasingTrend(unittest.TestCase):
    def test_increasing_trend_positive_numbers(self):
        self.assertTrue(increasing_trend([1, 2, 3, 4, 5]))

    def test_increasing_trend_negative_numbers(self):
        self.assertTrue(increasing_trend([-1, -2, -3, -4, -5]))

    def test_increasing_trend_mixed_numbers(self):
        self.assertTrue(increasing_trend([1, 2, 3, -4, 5]))

    def test_increasing_trend_descending_numbers(self):
        self.assertFalse(increasing_trend([5, 4, 3, 2, 1]))

    def test_increasing_trend_empty_list(self):
        self.assertFalse(increasing_trend([]))

    def test_increasing_trend_single_element_list(self):
        self.assertTrue(increasing_trend([1]))

    def test_increasing_trend_duplicates(self):
        self.assertTrue(increasing_trend([1, 1, 2, 2, 3]))
