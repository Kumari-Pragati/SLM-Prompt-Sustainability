import unittest
from mbpp_606_code import radian_degree

class TestRadianDegree(unittest.TestCase):
    def test_typical_cases(self):
        self.assertAlmostEqual(radian_degree(0), 0)
        self.assertAlmostEqual(radian_degree(90), math.pi / 2)
        self.assertAlmostEqual(radian_degree(180), math.pi)
        self.assertAlmostEqual(radian_degree(270), 3 * math.pi / 2)
        self.assertAlmostEqual(radian_degree(360), 2 * math.pi)

    def test_edge_and_boundary_cases(self):
        self.assertAlmostEqual(radian_degree(-360), -2 * math.pi)
        self.assertAlmostEqual(radian_degree(-180), -math.pi)
        self.assertAlmostEqual(radian_degree(-90), -math.pi / 2)
        self.assertAlmostEqual(radian_degree(-0), 0)
        self.assertAlmostEqual(radian_degree(361), 2 * math.pi + 1e-6)
        self.assertAlmostEqual(radian_degree(-361), -2 * math.pi - 1e-6)
