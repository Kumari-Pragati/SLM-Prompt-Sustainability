import unittest
from mbpp_606_code import radian_degree

class TestRadianDegree(unittest.TestCase):
    def test_typical_inputs(self):
        self.assertAlmostEqual(radian_degree(0), 0, places=5)
        self.assertAlmostEqual(radian_degree(90), math.pi/2, places=5)
        self.assertAlmostEqual(radian_degree(180), math.pi, places=5)
        self.assertAlmostEqual(radian_degree(270), 3*math.pi/2, places=5)
        self.assertAlmostEqual(radian_degree(360), 2*math.pi, places=5)

    def test_edge_cases(self):
        self.assertAlmostEqual(radian_degree(-180), -math.pi, places=5)
        self.assertAlmostEqual(radian_degree(-90), -math.pi/2, places=5)
        self.assertAlmostEqual(radian_degree(-0), 0, places=5)
        self.assertAlmostEqual(radian_degree(0), 0, places=5)
        self.assertAlmostEqual(radian_degree(450), 5*math.pi/2, places=5)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            radian_degree("a")
        with self.assertRaises(TypeError):
            radian_degree([1, 2, 3])

    def test_special_cases(self):
        self.assertAlmostEqual(radian_degree(360), 2*math.pi, places=5)
        self.assertAlmostEqual(radian_degree(-360), -2*math.pi, places=5)
