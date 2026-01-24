import unittest
from mbpp_670_code import decreasing_trend

class TestDecreasingTrend(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(decreasing_trend([5, 4, 3, 2, 1]))

    def test_typical_case_with_duplicates(self):
        self.assertTrue(decreasing_trend([5, 5, 4, 4, 3, 3, 2, 2, 1, 1]))

    def test_typical_case_with_same_numbers(self):
        self.assertTrue(decreasing_trend([1, 1, 1, 1, 1]))

    def test_edge_case_single_number(self):
        self.assertTrue(decreasing_trend([1]))

    def test_edge_case_empty_list(self):
        self.assertTrue(decreasing_trend([]))

    def test_typical_case_with_negative_numbers(self):
        self.assertTrue(decreasing_trend([-5, -4, -3, -2, -1]))

    def test_typical_case_with_mixed_numbers(self):
        self.assertFalse(decreasing_trend([5, 4, -3, -2, -1]))

    def test_edge_case_with_zero(self):
        self.assertFalse(decreasing_trend([0, 1]))

    def test_edge_case_with_same_negative_numbers(self):
        self.assertTrue(decreasing_trend([-1, -1, -1, -1, -1]))
