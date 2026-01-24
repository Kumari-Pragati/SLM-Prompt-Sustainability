import unittest
from mbpp_499_code import diameter_circle

class TestDiameterCircle(unittest.TestCase):

    def test_positive_radius(self):
        self.assertEqual(diameter_circle(5), 10)
        self.assertEqual(diameter_circle(10), 20)
        self.assertEqual(diameter_circle(15), 30)

    def test_zero_radius(self):
        self.assertEqual(diameter_circle(0), 0)

    def test_negative_radius(self):
        self.assertEqual(diameter_circle(-5), -10)
        self.assertEqual(diameter_circle(-10), -20)
