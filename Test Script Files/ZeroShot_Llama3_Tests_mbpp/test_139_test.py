import unittest
from mbpp_139_code import circle_circumference

class TestCircleCircumference(unittest.TestCase):

    def test_circle_circumference_positive_radius(self):
        self.assertAlmostEqual(circle_circumference(1), 6.283185307179586, places=5)

    def test_circle_circumference_zero_radius(self):
        self.assertAlmostEqual(circle_circumference(0), 0, places=5)

    def test_circle_circumference_negative_radius(self):
        with self.assertRaises(TypeError):
            circle_circumference(-1)

    def test_circle_circumference_non_numeric_radius(self):
        with self.assertRaises(TypeError):
            circle_circumference('a')
