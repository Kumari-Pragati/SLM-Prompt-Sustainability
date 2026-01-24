import unittest
from mbpp_606_code import radian_degree

class TestRadianDegree(unittest.TestCase):

    def test_typical_cases(self):
        self.assertAlmostEqual(radian_degree(0), 0)
        self.assertAlmostEqual(radian_degree(90), math.pi/2)
        self.assertAlmostEqual(radian_degree(180), math.pi)
        self.assertAlmostEqual(radian_degree(360), 2*math.pi)

    def test_edge_cases(self):
        self.assertAlmostEqual(radian_degree(-90), -math.pi/2)
        self.assertAlmostEqual(radian_degree(450), 2.5*math.pi)

    def test_boundary_cases(self):
        self.assertAlmostEqual(radian_degree(360), 2*math.pi)
        self.assertAlmostEqual(radian_degree(-360), -2*math.pi)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            radian_degree('90')
