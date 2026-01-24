import unittest
from mbpp_214_code import degree_radian

class TestDegreeRadian(unittest.TestCase):
    def test_typical_inputs(self):
        self.assertAlmostEqual(degree_radian(math.pi/2), 90.0)
        self.assertAlmostEqual(degree_radian(math.pi), 180.0)
        self.assertAlmostEqual(degree_radian(math.pi*3/2), 270.0)

    def test_edge_cases(self):
        self.assertAlmostEqual(degree_radian(0), 0.0)
        self.assertAlmostEqual(degree_radian(math.pi), 180.0)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            degree_radian("invalid input")

    def test_boundary_conditions(self):
        self.assertAlmostEqual(degree_radian(-math.pi), -180.0)
        self.assertAlmostEqual(degree_radian(math.pi), 180.0)
