import unittest
from mbpp_214_code import degree_radian

class TestDegreeRadian(unittest.TestCase):
    def test_positive_values(self):
        self.assertAlmostEqual(degree_radian(0), 0)
        self.assertAlmostEqual(degree_radian(math.pi/2), 90)
        self.assertAlmostEqual(degree_radian(math.pi), 180)
        self.assertAlmostEqual(degree_radian(3*math.pi/2), -90)
        self.assertAlmostEqual(degree_radian(2*math.pi), 360)

    def test_negative_values(self):
        self.assertAlmostEqual(degree_radian(-math.pi/2), -90)
        self.assertAlmostEqual(degree_radian(-math.pi), 180)
        self.assertAlmostEqual(degree_radian(-3*math.pi/2), 90)
        self.assertAlmostEqual(degree_radian(-2*math.pi), -360)

    def test_edge_cases(self):
        self.assertAlmostEqual(degree_radian(0.00000001), 0.00000001)
        self.assertAlmostEqual(degree_radian(math.pi - 1e-10), 180 - 1e-10)
        self.assertAlmostEqual(degree_radian(math.pi + 1e-10), 180 + 1e-10)
