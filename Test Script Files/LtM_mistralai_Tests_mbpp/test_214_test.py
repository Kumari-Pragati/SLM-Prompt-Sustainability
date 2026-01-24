import unittest
from mbpp_214_code import degree_radian

class TestDegreeRadian(unittest.TestCase):
    def test_simple_input(self):
        self.assertAlmostEqual(degree_radian(0), 0)
        self.assertAlmostEqual(degree_radian(math.pi / 2), 90)
        self.assertAlmostEqual(degree_radian(math.pi), 180)
        self.assertAlmostEqual(degree_radian(3 * math.pi / 2), -90)
        self.assertAlmostEqual(degree_radian(2 * math.pi), 360)

    def test_edge_and_boundary_conditions(self):
        self.assertAlmostEqual(degree_radian(-math.pi), -180)
        self.assertAlmostEqual(degree_radian(math.pi * 2), 720)
        self.assertAlmostEqual(degree_radian(math.inf), None)
        self.assertAlmostEqual(degree_radian(-math.inf), None)
