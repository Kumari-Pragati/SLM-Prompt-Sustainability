import unittest
from mbpp_139_code import circle_circumference

class TestCircleCircumference(unittest.TestCase):

    def test_positive_radius(self):
        self.assertAlmostEqual(circle_circumference(1), 6.283, places=3)

    def test_zero_radius(self):
        self.assertEqual(circle_circumference(0), 0)

    def test_negative_radius(self):
        self.assertEqual(circle_circumference(-1), 6.283)

    def test_large_radius(self):
        self.assertAlmostEqual(circle_circumference(1000), 6283.0, places=1)

    def test_float_radius(self):
        self.assertAlmostEqual(circle_circumference(2.5), 15.707, places=3)
