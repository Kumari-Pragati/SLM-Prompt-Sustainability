import unittest
from mbpp_85_code import surfacearea_sphere

class TestSurfaceAreaSphere(unittest.TestCase):

    def test_typical_case(self):
        self.assertAlmostEqual(surfacearea_sphere(5), 78.53981633974483)

    def test_edge_case(self):
        self.assertAlmostEqual(surfacearea_sphere(0), 0)

    def test_negative_radius(self):
        with self.assertRaises(TypeError):
            surfacearea_sphere(-1)

    def test_non_numeric_radius(self):
        with self.assertRaises(TypeError):
            surfacearea_sphere('a')

    def test_large_radius(self):
        self.assertAlmostEqual(surfacearea_sphere(100), 12566.53687229648)
