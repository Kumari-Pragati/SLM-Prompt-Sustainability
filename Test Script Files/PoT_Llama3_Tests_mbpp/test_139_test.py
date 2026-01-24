import unittest
from mbpp_139_code import circle_circumference

class TestCircleCircumference(unittest.TestCase):

    def test_typical_case(self):
        self.assertAlmostEqual(circle_circumference(5), 31.41592653589793)

    def test_edge_case(self):
        self.assertAlmostEqual(circle_circumference(0), 0)

    def test_edge_case(self):
        self.assertAlmostEqual(circle_circumference(1), 6.283185307179586)

    def test_edge_case(self):
        self.assertAlmostEqual(circle_circumference(10), 62.83185307179586)

    def test_edge_case(self):
        self.assertAlmostEqual(circle_circumference(-1), 6.283185307179586)

    def test_edge_case(self):
        self.assertAlmostEqual(circle_circumference(-10), 62.83185307179586)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            circle_circumference('a')
