import unittest
from mbpp_139_code import circle_circumference

class TestCircleCircumference(unittest.TestCase):
    def test_simple_inputs(self):
        self.assertAlmostEqual(circle_circumference(1), 6.283185307179586)
        self.assertAlmostEqual(circle_circumference(2), 12.566370614359172)
        self.assertAlmostEqual(circle_circumference(3), 18.84955641379472)

    def test_edge_and_boundary_conditions(self):
        self.assertAlmostEqual(circle_circumference(0), 0)
        self.assertAlmostEqual(circle_circumference(-1), -6.283185307179586)
        self.assertAlmostEqual(circle_circumference(0.5), 3.1415)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            circle_circumference('a')
        with self.assertRaises(TypeError):
            circle_circumference(None)
