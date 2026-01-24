import unittest
from mbpp_670_code import decreasing_trend

class TestDecreasingTrend(unittest.TestCase):

    def test_typical_cases(self):
        self.assertTrue(decreasing_trend([5, 4, 3, 2, 1]))
        self.assertTrue(decreasing_trend([10, 9, 8, 7, 6]))
        self.assertTrue(decreasing_trend([0]))

    def test_edge_and_boundary_cases(self):
        self.assertFalse(decreasing_trend([1, 2, 3, 4, 5]))
        self.assertFalse(decreasing_trend([5, 5, 4, 3, 2]))
        self.assertFalse(decreasing_trend([]))
        self.assertFalse(decreasing_trend([None]))
        self.assertFalse(decreasing_trend([1, 1, 1, 1, 1]))
