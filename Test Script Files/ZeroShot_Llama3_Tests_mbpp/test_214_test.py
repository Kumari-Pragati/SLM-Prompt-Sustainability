import unittest
from mbpp_214_code import degree_radian

class TestDegreeRadian(unittest.TestCase):

    def test_degree_radian_positive(self):
        self.assertAlmostEqual(degree_radian(math.pi/2), 90.0)
        self.assertAlmostEqual(degree_radian(math.pi), 180.0)
        self.assertAlmostEqual(degree_radian(math.pi*1.5), 270.0)

    def test_degree_radian_negative(self):
        self.assertAlmostEqual(degree_radian(-math.pi/2), -90.0)
        self.assertAlmostEqual(degree_radian(-math.pi), -180.0)
        self.assertAlmostEqual(degree_radian(-math.pi*1.5), -270.0)

    def test_degree_radian_zero(self):
        self.assertAlmostEqual(degree_radian(0), 0.0)
