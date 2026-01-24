import unittest
from mbpp_214_code import pi, radians

def degree_radian(radian):
    degree = radian * (180 / pi)
    return degree

class TestDegreeRadian(unittest.TestCase):

    def test_zero_radians(self):
        self.assertEqual(degree_radian(0), 0)

    def test_pi_radians(self):
        self.assertEqual(degree_radian(radians(pi)), 180)

    def test_negative_pi_radians(self):
        self.assertEqual(degree_radian(radians(-pi)), -180)

    def test_half_pi_radians(self):
        self.assertEqual(degree_radian(radians(pi / 2)), 90)

    def test_quarter_pi_radians(self):
        self.assertEqual(degree_radian(radians(pi / 4)), 45)
