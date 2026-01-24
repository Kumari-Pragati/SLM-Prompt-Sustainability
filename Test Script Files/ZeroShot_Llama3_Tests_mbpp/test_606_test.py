import unittest
from mbpp_606_code import radian_degree

class TestRadianDegree(unittest.TestCase):

    def test_radian_degree(self):
        self.assertAlmostEqual(radian_degree(0), 0, places=5)
        self.assertAlmostEqual(radian_degree(90), math.pi/2, places=5)
        self.assertAlmostEqual(radian_degree(180), math.pi, places=5)
        self.assertAlmostEqual(radian_degree(270), 3*math.pi/2, places=5)
        self.assertAlmostEqual(radian_degree(360), 2*math.pi, places=5)

        self.assertAlmostEqual(radian_degree(-90), -math.pi/2, places=5)
        self.assertAlmostEqual(radian_degree(-180), -math.pi, places=5)
        self.assertAlmostEqual(radian_degree(-270), -3*math.pi/2, places=5)
        self.assertAlmostEqual(radian_degree(-360), -2*math.pi, places=5)

        self.assertAlmostEqual(radian_degree(45), math.pi/4, places=5)
        self.assertAlmostEqual(radian_degree(-45), -math.pi/4, places=5)

        self.assertAlmostEqual(radian_degree(135), 3*math.pi/4, places=5)
        self.assertAlmostEqual(radian_degree(-135), -3*math.pi/4, places=5)

        self.assertAlmostEqual(radian_degree(225), 5*math.pi/4, places=5)
        self.assertAlmostEqual(radian_degree(-225), -5*math.pi/4, places=5)

        self.assertAlmostEqual(radian_degree(315), 7*math.pi/4, places=5)
        self.assertAlmostEqual(radian_degree(-315), -7*math.pi/4, places=5)
