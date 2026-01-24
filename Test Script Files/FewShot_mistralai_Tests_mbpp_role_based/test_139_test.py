import unittest
from mbpp_139_code import circle_circumference

class TestCircleCircumference(unittest.TestCase):
    def test_positive_radius(self):
        self.assertAlmostEqual(circle_circumference(3), 18.849555921538738)

    def test_zero_radius(self):
        self.assertEqual(circle_circumference(0), 0)

    def test_negative_radius(self):
        with self.assertRaises(ValueError):
            circle_circumference(-1)

    def test_small_radius(self):
        self.assertAlmostEqual(circle_circumference(0.1), 0.6283185307179586)
