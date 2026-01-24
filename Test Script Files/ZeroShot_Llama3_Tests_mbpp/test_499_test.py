import unittest
from mbpp_499_code import diameter_circle

class TestDiameterCircle(unittest.TestCase):

    def test_diameter_circle_positive(self):
        self.assertEqual(diameter_circle(5), 10)

    def test_diameter_circle_zero(self):
        self.assertEqual(diameter_circle(0), 0)

    def test_diameter_circle_negative(self):
        with self.assertRaises(TypeError):
            diameter_circle(-5)

    def test_diameter_circle_non_numeric(self):
        with self.assertRaises(TypeError):
            diameter_circle('five')
