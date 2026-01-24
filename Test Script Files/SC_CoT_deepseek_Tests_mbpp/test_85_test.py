import unittest
from mbpp_85_code import surfacearea_sphere

class TestSurfaceAreaSphere(unittest.TestCase):

    def test_typical_case(self):
        self.assertAlmostEqual(surfacearea_sphere(1), 12.566370614359172, places=7)

    def test_boundary_case(self):
        self.assertAlmostEqual(surfacearea_sphere(0), 0)

    def test_edge_case(self):
        self.assertAlmostEqual(surfacearea_sphere(0.5), 3.141592653589793)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            surfacearea_sphere("invalid")

        with self.assertRaises(ValueError):
            surfacearea_sphere(-1)
