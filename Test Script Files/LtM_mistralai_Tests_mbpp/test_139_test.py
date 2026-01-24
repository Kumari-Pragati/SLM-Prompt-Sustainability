import unittest
from mbpp_139_code import circle_circumference

class TestCircleCircumference(unittest.TestCase):
    def test_simple_input(self):
        self.assertAlmostEqual(circle_circumference(1), 6.283185307179586)

    def test_edge_input(self):
        self.assertAlmostEqual(circle_circumference(0), 0)
        self.assertAlmostEqual(circle_circumference(1e10), 6.283185307179586 * 1e10)

    def test_negative_input(self):
        self.assertAlmostEqual(circle_circumference(-1), -6.283185307179586)

    def test_complex_input(self):
        self.assertAlmostEqual(circle_circumference(0.5), 3.141592653589793)
