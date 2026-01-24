import unittest
from mbpp_606_code import radian_degree

class TestRadianDegree(unittest.TestCase):

    def test_simple_input(self):
        self.assertAlmostEqual(radian_degree(90), math.pi/2)

    def test_boundary_conditions(self):
        self.assertAlmostEqual(radian_degree(0), 0)
        self.assertAlmostEqual(radian_degree(360), 2*math.pi)

    def test_edge_cases(self):
        self.assertAlmostEqual(radian_degree(180), math.pi)
        self.assertAlmostEqual(radian_degree(-90), -math.pi/2)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            radian_degree('90')
