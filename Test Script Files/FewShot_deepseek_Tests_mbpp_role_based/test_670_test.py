import unittest
from mbpp_670_code import decreasing_trend

class TestDecreasingTrend(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertTrue(decreasing_trend([5, 4, 3, 2, 1]))

    def test_typical_use_case_with_duplicates(self):
        self.assertTrue(decreasing_trend([5, 5, 4, 4, 3, 3, 2, 2, 1, 1]))

    def test_edge_condition(self):
        self.assertTrue(decreasing_trend([1]))

    def test_boundary_condition(self):
        self.assertFalse(decreasing_trend([2, 1]))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            decreasing_trend("1, 2, 3")

        with self.assertRaises(TypeError):
            decreasing_trend(123)

        with self.assertRaises(TypeError):
            decreasing_trend(None)

        with self.assertRaises(TypeError):
            decreasing_trend([1, "2", 3])

        with self.assertRaises(TypeError):
            decreasing_trend([1, None, 3])
