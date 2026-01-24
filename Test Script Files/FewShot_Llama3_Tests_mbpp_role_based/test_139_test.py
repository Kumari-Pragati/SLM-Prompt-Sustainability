import unittest
from mbpp_139_code import circle_circumference

class TestCircleCircumference(unittest.TestCase):
    def test_positive_radius(self):
        self.assertAlmostEqual(circle_circumference(5), 31.41592653589793)

    def test_zero_radius(self):
        self.assertEqual(circle_circumference(0), 0)

    def test_negative_radius(self):
        with self.assertRaises(TypeError):
            circle_circumference(-5)

    def test_non_numeric_radius(self):
        with self.assertRaises(TypeError):
            circle_circumference('five')
