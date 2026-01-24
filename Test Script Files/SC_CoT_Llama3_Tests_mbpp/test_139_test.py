import unittest
from mbpp_139_code import circle_circumference

class TestCircleCircumference(unittest.TestCase):
    def test_typical_input(self):
        self.assertAlmostEqual(circle_circumference(5), 31.41592653589793, places=5)

    def test_zero_radius(self):
        with self.assertRaises(ZeroDivisionError):
            circle_circumference(0)

    def test_negative_radius(self):
        with self.assertRaises(TypeError):
            circle_circumference(-5)

    def test_non_numeric_radius(self):
        with self.assertRaises(TypeError):
            circle_circumference('five')

    def test_edge_case(self):
        self.assertAlmostEqual(circle_circumference(1), 6.283185307179586, places=5)

    def test_large_radius(self):
        self.assertAlmostEqual(circle_circumference(100), 628.318530717959, places=5)
