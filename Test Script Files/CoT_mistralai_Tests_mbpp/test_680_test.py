import unittest
from mbpp_680_code import increasing_trend

class TestIncreasingTrend(unittest.TestCase):
    def test_empty_list(self):
        self.assertTrue(increasing_trend([]))

    def test_single_element(self):
        self.assertTrue(increasing_trend([1]))
        self.assertFalse(increasing_trend([0]))

    def test_increasing_sequence(self):
        self.assertTrue(increasing_trend([1, 2, 3, 4, 5]))
        self.assertTrue(increasing_trend([-1, -2, -3, -4, -5]))

    def test_decreasing_sequence(self):
        self.assertFalse(increasing_trend([5, 4, 3, 2, 1]))
        self.assertFalse(increasing_trend([-5, -4, -3, -2, -1]))

    def test_duplicates(self):
        self.assertTrue(increasing_trend([1, 1, 2, 3]))
        self.assertFalse(increasing_trend([3, 2, 1, 1]))

    def test_mixed_sequence(self):
        self.assertTrue(increasing_trend([1, 0, 2, 3]))
        self.assertFalse(increasing_trend([3, 2, 1, 0]))

    def test_invalid_input(self):
        self.assertRaises(TypeError, increasing_trend, 123)
        self.assertRaises(TypeError, increasing_trend, ('str'))
