import unittest
from mbpp_670_code import decreasing_trend

class TestDecreasingTrend(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertTrue(decreasing_trend([5, 4, 3, 2, 1]))
        self.assertTrue(decreasing_trend([10, 9, 8, 7, 6]))

    def test_edge_conditions(self):
        self.assertTrue(decreasing_trend([1]))
        self.assertTrue(decreasing_trend([]))

    def test_boundary_conditions(self):
        self.assertFalse(decreasing_trend([2, 1, 2]))
        self.assertFalse(decreasing_trend([1, 2, 3]))

    def test_complex_cases(self):
        self.assertFalse(decreasing_trend([5, 4, 3, 3, 2, 1]))
        self.assertFalse(decreasing_trend([10, 9, 9, 8, 7, 6]))
