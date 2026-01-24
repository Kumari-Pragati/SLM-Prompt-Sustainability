import unittest
from mbpp_606_code import radian_degree

class TestRadianDegree(unittest.TestCase):

    def test_typical_case(self):
        self.assertAlmostEqual(radian_degree(90), math.pi/2)

    def test_boundary_case(self):
        self.assertAlmostEqual(radian_degree(0), 0)

    def test_edge_case(self):
        self.assertAlmostEqual(radian_degree(360), 2*math.pi)

    def test_negative_degree(self):
        self.assertAlmostEqual(radian_degree(-90), -math.pi/2)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            radian_degree('90')
