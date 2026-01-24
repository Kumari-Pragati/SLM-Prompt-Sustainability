import unittest
from mbpp_214_code import degree_radian

class TestDegreeRadian(unittest.TestCase):
    def test_typical_inputs(self):
        self.assertAlmostEqual(degree_radian(math.pi/2), 90.0)
        self.assertAlmostEqual(degree_radian(math.pi), 180.0)
        self.assertAlmostEqual(degree_radian(math.pi/4), 45.0)

    def test_edge_cases(self):
        self.assertAlmostEqual(degree_radian(0), 0.0)
        self.assertAlmostEqual(degree_radian(math.pi/2), 90.0)
        self.assertAlmostEqual(degree_radian(math.pi), 180.0)
        self.assertAlmostEqual(degree_radian(2*math.pi), 360.0)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            degree_radian("invalid input")
        with self.assertRaises(TypeError):
            degree_radian([1, 2, 3])

    def test_boundary_cases(self):
        self.assertAlmostEqual(degree_radian(-math.pi), -180.0)
        self.assertAlmostEqual(degree_radian(math.pi), 180.0)
        self.assertAlmostEqual(degree_radian(-2*math.pi), -360.0)
        self.assertAlmostEqual(degree_radian(2*math.pi), 360.0)
