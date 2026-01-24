import unittest
from mbpp_680_code import increasing_trend

class TestIncreasingTrend(unittest.TestCase):

    def test_empty_list(self):
        self.assertTrue(increasing_trend([]))

    def test_single_element(self):
        self.assertTrue(increasing_trend([1]))

    def test_decreasing_list(self):
        self.assertFalse(increasing_trend([2, 1]))

    def test_increasing_list(self):
        self.assertTrue(increasing_trend([1, 2, 3]))

    def test_duplicates(self):
        self.assertTrue(increasing_trend([1, 1, 2, 3]))

    def test_complex_list(self):
        self.assertTrue(increasing_trend([-1, 0, 1, 2, 3]))
