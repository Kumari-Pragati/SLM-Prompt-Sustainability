import unittest
from mbpp_85_code import surfacearea_sphere

class TestSurfaceAreaSphere(unittest.TestCase):
    def test_typical_inputs(self):
        self.assertAlmostEqual(surfacearea_sphere(1), 12.566370614359272)

    def test_edge_cases(self):
        self.assertAlmostEqual(surfacearea_sphere(0), 0)
        self.assertAlmostEqual(surfacearea_sphere(float('inf')), float('inf'))

    def test_negative_input(self):
        with self.assertRaises(TypeError):
            surfacearea_sphere(-1)

    def test_non_numeric_input(self):
        with self.assertRaises(TypeError):
            surfacearea_sphere('a')

    def test_zero_input(self):
        self.assertAlmostEqual(surfacearea_sphere(0), 0)

    def test_large_input(self):
        self.assertAlmostEqual(surfacearea_sphere(10), 1256.7431659345927)
