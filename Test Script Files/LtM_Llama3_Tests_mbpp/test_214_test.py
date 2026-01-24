import unittest
from mbpp_214_code import degree_radian

class TestDegreeRadian(unittest.TestCase):
    def test_simple_inputs(self):
        self.assertEqual(degree_radian(0), 0)
        self.assertEqual(degree_radian(math.pi/2), 90)
        self.assertEqual(degree_radian(math.pi), 180)
        self.assertEqual(degree_radian(2*math.pi), 360)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(degree_radian(-math.pi), -180)
        self.assertEqual(degree_radian(math.pi/2 + 0.0001), 90)
        self.assertEqual(degree_radian(math.pi + 0.0001), 180)
        self.assertEqual(degree_radian(2*math.pi + 0.0001), 360)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            degree_radian("test")
        with self.assertRaises(TypeError):
            degree_radian(None)
