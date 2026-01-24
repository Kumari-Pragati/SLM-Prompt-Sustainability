import unittest
from mbpp_85_code import pi
from85_code import surfacearea_sphere

class TestSurfaceAreaSphere(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(surfacearea_sphere(3), round(4 * pi * 9, 2))

    def test_edge_case_zero(self):
        self.assertEqual(surfacearea_sphere(0), 0)

    def test_edge_case_negative(self):
        self.assertEqual(surfacearea_sphere(-1), -4 * pi)

    def test_edge_case_one(self):
        self.assertAlmostEqual(surfacearea_sphere(1), round(4 * pi, 2))
