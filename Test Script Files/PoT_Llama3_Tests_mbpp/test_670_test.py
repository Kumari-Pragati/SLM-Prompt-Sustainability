import unittest
from mbpp_670_code import decreasing_trend

class TestDecreasingTrend(unittest.TestCase):
    def test_typical_case(self):
        self.assertTrue(decreasing_trend([1, 2, 3]))

    def test_edge_case_descending(self):
        self.assertTrue(decreasing_trend([5, 4, 3, 2, 1]))

    def test_edge_case_ascending(self):
        self.assertFalse(decreasing_trend([1, 2, 3, 4, 5]))

    def test_edge_case_equal(self):
        self.assertTrue(decreasing_trend([1, 1, 1]))

    def test_edge_case_empty(self):
        self.assertTrue(decreasing_trend([]))

    def test_edge_case_single_element(self):
        self.assertTrue(decreasing_trend([1]))

    def test_edge_case_single_element_descending(self):
        self.assertTrue(decreasing_trend([5]))

    def test_edge_case_single_element_ascending(self):
        self.assertFalse(decreasing_trend([1]))

    def test_edge_case_single_element_equal(self):
        self.assertTrue(decreasing_trend([1]))

    def test_edge_case_descending_with_duplicates(self):
        self.assertTrue(decreasing_trend([5, 4, 4, 3, 2, 1]))

    def test_edge_case_ascending_with_duplicates(self):
        self.assertFalse(decreasing_trend([1, 2, 2, 3, 4, 5]))

    def test_edge_case_equal_with_duplicates(self):
        self.assertTrue(decreasing_trend([1, 1, 1, 1]))
