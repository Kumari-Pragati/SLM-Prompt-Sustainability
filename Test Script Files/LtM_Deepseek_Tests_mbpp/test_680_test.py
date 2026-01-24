import unittest
from mbpp_680_code import increasing_trend

class TestIncreasingTrend(unittest.TestCase):

    def test_simple_increasing_trend(self):
        self.assertTrue(increasing_trend([1, 2, 3, 4, 5]))

    def test_simple_decreasing_trend(self):
        self.assertFalse(increasing_trend([5, 4, 3, 2, 1]))

    def test_empty_list(self):
        self.assertTrue(increasing_trend([]))

    def test_single_element(self):
        self.assertTrue(increasing_trend([1]))

    def test_already_sorted_list(self):
        self.assertTrue(increasing_trend([1, 2, 3, 4, 5]))

    def test_already_sorted_in_reverse_list(self):
        self.assertFalse(increasing_trend([5, 4, 3, 2, 1]))

    def test_duplicate_elements(self):
        self.assertTrue(increasing_trend([1, 1, 2, 3, 4]))

    def test_negative_numbers(self):
        self.assertTrue(increasing_trend([-5, -4, -3, -2, -1]))

    def test_mixed_numbers(self):
        self.assertFalse(increasing_trend([1, -1, 2, -2, 3]))
