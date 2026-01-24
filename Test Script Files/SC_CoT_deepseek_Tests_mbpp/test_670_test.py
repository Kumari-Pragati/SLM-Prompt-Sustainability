import unittest
from mbpp_670_code import decreasing_trend

class TestDecreasingTrend(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(decreasing_trend([5, 4, 3, 2, 1]))

    def test_typical_case_with_duplicates(self):
        self.assertTrue(decreasing_trend([5, 5, 4, 4, 3, 3, 2, 2, 1, 1]))

    def test_edge_case_single_element(self):
        self.assertTrue(decreasing_trend([1]))

    def test_edge_case_empty_list(self):
        self.assertTrue(decreasing_trend([]))

    def test_edge_case_negative_numbers(self):
        self.assertTrue(decreasing_trend([-5, -4, -3, -2, -1]))

    def test_edge_case_duplicates_and_negative_numbers(self):
        self.assertTrue(decreasing_trend([5, 5, 4, 4, 3, 3, 2, 2, 1, 1, -1, -1]))

    def test_corner_case_same_numbers(self):
        self.assertTrue(decreasing_trend([1, 1, 1, 1, 1]))

    def test_invalid_input_non_numeric(self):
        with self.assertRaises(TypeError):
            decreasing_trend(['a', 'b', 'c'])

    def test_invalid_input_non_list(self):
        with self.assertRaises(TypeError):
            decreasing_trend('12345')
