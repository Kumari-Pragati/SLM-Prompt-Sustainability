import unittest
from mbpp_606_code import radian_degree

class TestRadianDegree(unittest.TestCase):
    def test_positive_degrees(self):
        self.assertAlmostEqual(radian_degree(0), 0)
        self.assertAlmostEqual(radian_degree(90), math.pi/2)
        self.assertAlmostEqual(radian_degree(180), math.pi)
        self.assertAlmostEqual(radian_degree(270), 3*math.pi/2)
        self.assertAlmostEqual(radian_degree(360), 2*math.pi)

    def test_negative_degrees(self):
        self.assertAlmostEqual(radian_degree(-180), -math.pi)
        self.assertAlmostEqual(radian_degree(-270), -3*math.pi/2)
        self.assertAlmostEqual(radian_degree(-360), -2*math.pi)

    def test_zero_degree(self):
        self.assertAlmostEqual(radian_degree(0), 0)

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            radian_degree(-400)
        with self.assertRaises(ValueError):
            radian_degree(900)
