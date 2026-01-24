import unittest
from mbpp_670_code import decreasing_trend

class TestDecreasingTrend(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(decreasing_trend([5, 4, 3, 2, 1]))

    def test_empty_list(self):
        self.assertTrue(decreasing_trend([]))

    def test_single_element(self):
        self.assertTrue(decreasing_trend([1]))

    def test_same_elements(self):
        self.assertTrue(decreasing_trend([1, 1, 1, 1]))

    def test_increasing_trend(self):
        self.assertFalse(decreasing_trend([1, 2, 3, 4, 5]))

    def test_random_elements(self):
        self.assertFalse(decreasing_trend([3, 2, 5, 1, 4]))

    def test_negative_numbers(self):
        self.assertTrue(decreasing_trend([-5, -4, -3, -2, -1]))

    def test_mixed_numbers(self):
        self.assertFalse(decreasing_trend([5, -4, 3, -2, 1]))
