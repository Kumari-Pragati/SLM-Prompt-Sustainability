import unittest
from mbpp_680_code import increasing_trend

class TestIncreasingTrend(unittest.TestCase):
    def test_typical_case(self):
        self.assertTrue(increasing_trend([1, 2, 3, 4, 5]))

    def test_edge_case(self):
        self.assertTrue(increasing_trend([1]))

    def test_boundary_case(self):
        self.assertFalse(increasing_trend([3, 2, 1]))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            increasing_trend("1, 2, 3, 4, 5")

    def test_empty_list(self):
        self.assertTrue(increasing_trend([]))
