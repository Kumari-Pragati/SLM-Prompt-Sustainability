import unittest
from mbpp_214_code import degree_radian

class TestDegreeRadian(unittest.TestCase):
    def test_normal_input(self):
        self.assertAlmostEqual(degree_radian(math.pi / 2), 90)
        self.assertAlmostEqual(degree_radian(math.pi), 180)
        self.assertAlmostEqual(degree_radian(3 * math.pi / 2), -90)

    def test_edge_and_boundary_conditions(self):
        self.assertAlmostEqual(degree_radian(0), 0)
        self.assertAlmostEqual(degree_radian(math.pi / 4), 45)
        self.assertAlmostEqual(degree_radian(math.pi / 8), 11.25)
        self.assertAlmostEqual(degree_radian(-math.pi), -180)
        self.assertAlmostEqual(degree_radian(-math.pi / 2), -90)

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, degree_radian, 'invalid string')
        self.assertRaises(TypeError, degree_radian, 123)
