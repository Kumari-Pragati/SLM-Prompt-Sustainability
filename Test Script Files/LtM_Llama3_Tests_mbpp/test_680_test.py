import unittest
from mbpp_680_code import increasing_trend

class TestIncreasingTrend(unittest.TestCase):
    def test_simple_true(self):
        self.assertTrue(increasing_trend([1, 2, 3, 4, 5]))

    def test_simple_false(self):
        self.assertFalse(increasing_trend([5, 4, 3, 2, 1]))

    def test_empty_list(self):
        self.assertFalse(increasing_trend([]))

    def test_single_element_list(self):
        self.assertTrue(increasing_trend([1]))

    def test_single_element_list_false(self):
        self.assertFalse(increasing_trend([5]))

    def test_all_equal(self):
        self.assertTrue(increasing_trend([1, 1, 1, 1, 1]))

    def test_all_equal_false(self):
        self.assertFalse(increasing_trend([1, 2, 3, 4, 5]))

    def test_reversed_list(self):
        self.assertFalse(increasing_trend([5, 4, 3, 2, 1]))

    def test_reversed_list_true(self):
        self.assertTrue(increasing_trend([1, 2, 3, 4, 5]))
