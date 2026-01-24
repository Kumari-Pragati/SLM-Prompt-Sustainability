import unittest
from mbpp_606_code import radian_degree

class TestRadianDegree(unittest.TestCase):
    def test_simple_inputs(self):
        self.assertAlmostEqual(radian_degree(0), 0)
        self.assertAlmostEqual(radian_degree(90), math.pi/2)
        self.assertAlmostEqual(radian_degree(180), math.pi)
        self.assertAlmostEqual(radian_degree(270), 3*math.pi/2)
        self.assertAlmostEqual(radian_degree(360), 2*math.pi)

    def test_edge_cases(self):
        self.assertAlmostEqual(radian_degree(-180), -math.pi)
        self.assertAlmostEqual(radian_degree(540), 3*math.pi)
        self.assertAlmostEqual(radian_degree(-720), -2*math.pi)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            radian_degree("hello")
        with self.assertRaises(TypeError):
            radian_degree(None)
