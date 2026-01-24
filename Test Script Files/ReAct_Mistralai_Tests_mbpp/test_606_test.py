import unittest
from mbpp_606_code import radian_degree

class TestRadianDegree(unittest.TestCase):

    def test_radian_degree_positive(self):
        # Typical case: positive degree value
        self.assertAlmostEqual(radian_degree(0), 0)
        self.assertAlmostEqual(radian_degree(90), math.pi/2)
        self.assertAlmostEqual(radian_degree(180), math.pi)
        self.assertAlmostEqual(radian_degree(270), 3*math.pi/2)
        self.assertAlmostEqual(radian_degree(360), 2*math.pi)

    def test_radian_degree_negative(self):
        # Typical case: negative degree value
        self.assertAlmostEqual(radian_degree(-0), 0)
        self.assertAlmostEqual(radian_degree(-90), -math.pi/2)
        self.assertAlmostEqual(radian_degree(-180), -math.pi)
        self.assertAlmostEqual(radian_degree(-270), -3*math.pi/2)
        self.assertAlmostEqual(radian_degree(-360), -2*math.pi)

    def test_radian_degree_zero(self):
        # Edge case: zero degree value
        self.assertAlmostEqual(radian_degree(0), 0)

    def test_radian_degree_out_of_range(self):
        # Edge case: out-of-range degree value
        self.assertRaises(ValueError, radian_degree, 361)
        self.assertRaises(ValueError, radian_degree, -361)
