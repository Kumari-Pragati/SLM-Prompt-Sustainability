import unittest
from mbpp_139_code import circle_circumference

class TestCircleCircumference(unittest.TestCase):

    def test_positive_radius(self):
        self.assertAlmostEqual(circle_circumference(1), 6.283, places=3)
        self.assertAlmostEqual(circle_circumference(5), 31.415, places=3)

    def test_zero_radius(self):
        self.assertEqual(circle_circumference(0), 0)

    def test_negative_radius(self):
        self.assertEqual(circle_circumference(-1), 0)

    def test_non_numeric_input(self):
        with self.assertRaises(TypeError):
            circle_circumference('a')
