import unittest
from mbpp_139_code import pi

def circle_circumference(r):
  perimeter=2*pi*r
  return perimeter

class TestCircleCircumference(unittest.TestCase):

    def test_zero_radius(self):
        with self.assertRaises(ValueError):
            circle_circumference(0)

    def test_positive_radius(self):
        self.assertAlmostEqual(circle_circumference(1), 2 * pi)
        self.assertAlmostEqual(circle_circumference(2), 4 * pi)
        self.assertAlmostEqual(circle_circumference(3), 6 * pi)

    def test_negative_radius(self):
        with self.assertRaises(ValueError):
            circle_circumference(-1)
