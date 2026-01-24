import unittest
from mbpp_606_code import pi
from your_module import radian_degree  # replace 'your_module' with the actual module name where the function is defined

class TestRadianDegree(unittest.TestCase):

    def test_radian_degree_0(self):
        self.assertAlmostEqual(radian_degree(0), 0, delta=1e-6)

    def test_radian_degree_90(self):
        self.assertAlmostEqual(radian_degree(90), pi / 2, delta=1e-6)

    def test_radian_degree_180(self):
        self.assertAlmostEqual(radian_degree(180), pi, delta=1e-6)

    def test_radian_degree_270(self):
        self.assertAlmostEqual(radian_degree(270), 3 * pi / 2, delta=1e-6)

    def test_radian_degree_360(self):
        self.assertAlmostEqual(radian_degree(360), 2 * pi, delta=1e-6)

    def test_radian_degree_negative_90(self):
        self.assertAlmostEqual(radian_degree(-90), -pi / 2, delta=1e-6)

    def test_radian_degree_negative_180(self):
        self.assertAlmostEqual(radian_degree(-180), pi, delta=1e-6)
