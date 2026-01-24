import unittest
from mbpp_85_code import surfacearea_sphere

class TestSurfaceAreaSphere(unittest.TestCase):
    def test_simple_inputs(self):
        self.assertAlmostEqual(surfacearea_sphere(1), 12.566370614359272)
        self.assertAlmostEqual(surfacearea_sphere(2), 50.26548245743669)
        self.assertAlmostEqual(surfacearea_sphere(3), 113.09733552923254)

    def test_edge_cases(self):
        self.assertAlmostEqual(surfacearea_sphere(0), 0)
        self.assertAlmostEqual(surfacearea_sphere(-1), 12.566370614359272)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            surfacearea_sphere("a")
        with self.assertRaises(TypeError):
            surfacearea_sphere(None)
