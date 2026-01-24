import unittest
from mbpp_606_code import radian_degree

class TestRadianDegree(unittest.TestCase):

    def test_typical_case(self):
        self.assertAlmostEqual(radian_degree(45), math.pi/4)

    def test_edge_case(self):
        self.assertAlmostEqual(radian_degree(0), 0)

    def test_edge_case2(self):
        self.assertAlmostEqual(radian_degree(360), 2*math.pi)

    def test_edge_case3(self):
        self.assertAlmostEqual(radian_degree(-45), -math.pi/4)

    def test_edge_case4(self):
        self.assertAlmostEqual(radian_degree(90), math.pi/2)

    def test_edge_case5(self):
        self.assertAlmostEqual(radian_degree(270), 3*math.pi/2)

    def test_edge_case6(self):
        self.assertAlmostEqual(radian_degree(-90), -math.pi/2)

    def test_edge_case7(self):
        self.assertAlmostEqual(radian_degree(180), math.pi)

    def test_edge_case8(self):
        self.assertAlmostEqual(radian_degree(-180), -math.pi)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            radian_degree('abc')
