import unittest
from mbpp_606_code import radian_degree
import math

class TestRadianDegree(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertAlmostEqual(radian_degree(90), math.pi/2)

    def test_boundary_condition(self):
        self.assertAlmostEqual(radian_degree(0), 0)

    def test_edge_condition(self):
        self.assertAlmostEqual(radian_degree(180), math.pi)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            radian_degree('90')
