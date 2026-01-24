import unittest
from mbpp_680_code import increasing_trend

class TestIncreasingTrend(unittest.TestCase):

    def test_normal_input(self):
        self.assertTrue(increasing_trend([1, 2, 3, 4, 5]))
        self.assertTrue(increasing_trend([-1, -2, -3, -4, -5]))
        self.assertTrue(increasing_trend([0, 1, 2, 3, 4]))

    def test_edge_and_boundary_cases(self):
        self.assertTrue(increasing_trend([1, 2, 3, 4, 5, 6]))
        self.assertTrue(increasing_trend([-1, -2, -3, -4, -5, -6]))
        self.assertTrue(increasing_trend([0, 0, 1, 2, 3, 4]))
        self.assertFalse(increasing_trend([1, 2, 3, 4, 4, 5]))
        self.assertFalse(increasing_trend([-1, -2, -3, -4, -5, -6, -7]))
        self.assertFalse(increasing_trend([0, 0, 0, 1, 2, 3, 4]))

    def test_decreasing_input(self):
        self.assertFalse(increasing_trend([5, 4, 3, 2, 1]))
        self.assertFalse(increasing_trend([-5, -4, -3, -2, -1]))
        self.assertFalse(increasing_trend([0, 1, 2, 3, 4, 5]))

    def test_duplicate_values(self):
        self.assertFalse(increasing_trend([1, 1, 2, 3]))
        self.assertFalse(increasing_trend([-1, -1, -2, -3]))
        self.assertFalse(increasing_trend([0, 0, 1, 2]))
