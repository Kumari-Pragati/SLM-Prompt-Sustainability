import unittest
from mbpp_680_code import increasing_trend

class TestIncreasingTrend(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(increasing_trend([1, 2, 3, 4, 5]))

    def test_empty_list(self):
        self.assertTrue(increasing_trend([]))

    def test_single_element(self):
        self.assertTrue(increasing_trend([1]))

    def test_decreasing_order(self):
        self.assertFalse(increasing_trend([5, 4, 3, 2, 1]))

    def test_same_elements(self):
        self.assertTrue(increasing_trend([1, 1, 1, 1]))

    def test_negative_numbers(self):
        self.assertTrue(increasing_trend([-5, -4, -3, -2, -1]))

    def test_mixed_numbers(self):
        self.assertFalse(increasing_trend([1, 3, 2, 4]))

    def test_float_numbers(self):
        self.assertTrue(increasing_trend([1.0, 2.0, 3.0]))

    def test_mixed_float_numbers(self):
        self.assertFalse(increasing_trend([1.0, 2.0, 2.5, 3.0]))
