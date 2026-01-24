import unittest
from mbpp_680_code import increasing_trend

class TestIncreasingTrend(unittest.TestCase):

    def test_increasing_trend_true(self):
        self.assertTrue(increasing_trend([1, 2, 3, 4, 5]))

    def test_increasing_trend_false(self):
        self.assertFalse(increasing_trend([5, 4, 3, 2, 1]))

    def test_increasing_trend_same_elements(self):
        self.assertTrue(increasing_trend([1, 1, 1, 1, 1]))

    def test_increasing_trend_empty_list(self):
        self.assertTrue(increasing_trend([]))

    def test_increasing_trend_single_element(self):
        self.assertTrue(increasing_trend([1]))
