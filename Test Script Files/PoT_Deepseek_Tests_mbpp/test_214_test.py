import unittest
from mbpp_214_code import degree_radian

class TestDegreeRadian(unittest.TestCase):

    def test_typical_cases(self):
        self.assertAlmostEqual(degree_radian(0), 0)
        self.assertAlmostEqual(degree_radian(math.pi), 180)
        self.assertAlmostEqual(degree_radian(math.pi/2), 90)

    def test_edge_cases(self):
        self.assertAlmostEqual(degree_radian(math.pi*2), 360)
        self.assertAlmostEqual(degree_radian(math.pi/4), 45)
        self.assertAlmostEqual(degree_radian(math.pi/6), 30)

    def test_boundary_conditions(self):
        self.assertAlmostEqual(degree_radian(math.pi/180), 1)
        self.assertAlmostEqual(degree_radian(math.pi*180), 360*180)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            degree_radian('invalid')
        with self.assertRaises(TypeError):
            degree_radian(None)
