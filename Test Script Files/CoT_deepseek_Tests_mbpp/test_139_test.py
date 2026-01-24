import unittest
from mbpp_139_code import circle_circumference

class TestCircleCircumference(unittest.TestCase):

    def test_typical_case(self):
        self.assertAlmostEqual(circle_circumference(5), 31.415, places=3)

    def test_small_radius(self):
        self.assertAlmostEqual(circle_circumference(0.1), 0.6283, places=3)

    def test_large_radius(self):
        self.assertAlmostEqual(circle_circumference(100), 628.3, places=3)

    def test_negative_radius(self):
        with self.assertRaises(Exception):
            circle_circumference(-5)

    def test_non_numeric_input(self):
        with self.assertRaises(Exception):
            circle_circumference('a')
