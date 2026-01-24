import unittest
from mbpp_670_code import decreasing_trend

class TestDecreasingTrend(unittest.TestCase):

    def test_simple_decreasing(self):
        self.assertTrue(decreasing_trend([5, 4, 3, 2, 1]))

    def test_simple_increasing(self):
        self.assertFalse(decreasing_trend([1, 2, 3, 4, 5]))

    def test_simple_same(self):
        self.assertTrue(decreasing_trend([1, 1, 1]))

    def test_empty_list(self):
        self.assertFalse(decreasing_trend([]))

    def test_single_element(self):
        self.assertTrue(decreasing_trend([1]))

    def test_duplicate_elements(self):
        self.assertTrue(decreasing_trend([1, 1, 2, 1]))

    def test_edge_case_min(self):
        self.assertTrue(decreasing_trend([-100, -99, -98]))

    def test_edge_case_max(self.test_edge_case_min):
        self.assertTrue(decreasing_trend([100, 99, 98]))
