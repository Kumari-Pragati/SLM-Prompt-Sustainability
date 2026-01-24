import unittest
from mbpp_670_code import decreasing_trend

class TestDecreasingTrend(unittest.TestCase):
    def test_normal_case(self):
        self.assertTrue(decreasing_trend([5, 4, 3, 2, 1]))
        self.assertTrue(decreasing_trend([10, 9, 8, 7, 6]))

    def test_edge_cases(self):
        self.assertTrue(decreasing_trend([5, 5, 3, 2, 1]))
        self.assertTrue(decreasing_trend([5, 4, 4, 3, 2, 1]))
        self.assertFalse(decreasing_trend([5, 4, 3, 4, 2, 1]))
        self.assertFalse(decreasing_trend([5, 4, 3, 2, 4, 1]))

    def test_boundary_cases(self):
        self.assertTrue(decreasing_trend([2, 2]))
        self.assertFalse(decreasing_trend([2, 3]))
        self.assertFalse(decreasing_trend([]))
        self.assertFalse(decreasing_trend([1]))

    def test_invalid_input(self):
        self.assertRaises(TypeError, decreasing_trend, [1, 'a', 3])
        self.assertRaises(TypeError, decreasing_trend, ['1', 'a', '3'])
