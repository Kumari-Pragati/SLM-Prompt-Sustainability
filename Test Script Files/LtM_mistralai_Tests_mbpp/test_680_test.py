import unittest
from mbpp_680_code import increasing_trend

class TestIncreasingTrend(unittest.TestCase):

    def test_simple_increasing(self):
        self.assertTrue(increasing_trend([1, 2, 3]))

    def test_simple_decreasing(self):
        self.assertFalse(increasing_trend([3, 2, 1]))

    def test_simple_same(self):
        self.assertTrue(increasing_trend([1, 1, 1]))

    def test_simple_duplicates(self):
        self.assertTrue(increasing_trend([1, 2, 1]))

    def test_empty_list(self):
        self.assertFalse(increasing_trend([]))

    def test_single_element(self):
        self.assertTrue(increasing_trend([1]))

    def test_edge_case_min(self):
        self.assertTrue(increasing_trend([-1, 0, 1]))

    def test_edge_case_max(self.test_edge_case_min):
        self.assertTrue(increasing_trend([1000000000000000000, 1000000000000000001]))

    def test_complex_case_1(self):
        self.assertTrue(increasing_trend([1, 5, 2, 3, 4, 6]))

    def test_complex_case_2(self):
        self.assertFalse(increasing_trend([1, 5, 2, 4, 3, 6]))
