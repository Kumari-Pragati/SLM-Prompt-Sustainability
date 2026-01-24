import unittest
from mbpp_499_code import diameter_circle

class TestDiameterCircle(unittest.TestCase):
    def test_positive_radius(self):
        self.assertEqual(diameter_circle(3.14), 6.28)

    def test_zero_radius(self):
        self.assertEqual(diameter_circle(0), 0)

    def test_negative_radius(self):
        with self.assertRaises(ValueError):
            diameter_circle(-1)

    def test_non_numeric_radius(self):
        with self.assertRaises(TypeError):
            diameter_circle('string')
