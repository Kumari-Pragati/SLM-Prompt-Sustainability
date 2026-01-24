import unittest
from mbpp_761_code import arc_length

class TestArcLength(unittest.TestCase):
    def test_valid_input(self):
        self.assertAlmostEqual(arc_length(10, 90), 8.8274508, places=5)

    def test_invalid_input(self):
        self.assertIsNone(arc_length(10, 400))

    def test_edge_case(self):
        self.assertAlmostEqual(arc_length(10, 360), 31.41666667, places=5)

    def test_zero_input(self):
        self.assertIsNone(arc_length(0, 90))

    def test_negative_input(self):
        with self.assertRaises(TypeError):
            arc_length(-10, 90)

    def test_non_numeric_input(self):
        with self.assertRaises(TypeError):
            arc_length('a', 90)
