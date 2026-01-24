import unittest
from mbpp_139_code import circle_circumference

class TestCircleCircumference(unittest.TestCase):

    def test_typical_case(self):
        self.assertAlmostEqual(circle_circumference(5), 31.415, places=3)

    def test_boundary_case(self):
        self.assertAlmostEqual(circle_circumference(0), 0)

    def test_edge_case(self):
        self.assertAlmostEqual(circle_circumference(1), 6.283, places=3)

    def test_negative_radius(self):
        with self.assertRaises(ValueError):
            circle_circumference(-5)
