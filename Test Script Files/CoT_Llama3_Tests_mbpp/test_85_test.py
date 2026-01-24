import unittest
from mbpp_85_code import surfacearea_sphere

class TestSurfaceAreaSphere(unittest.TestCase):
    def test_typical_input(self):
        self.assertAlmostEqual(surfacearea_sphere(5), 78.53981633974483)

    def test_edge_case_zero(self):
        self.assertAlmostEqual(surfacearea_sphere(0), 0)

    def test_edge_case_negative(self):
        with self.assertRaises(TypeError):
            surfacearea_sphere(-5)

    def test_edge_case_non_numeric(self):
        with self.assertRaises(TypeError):
            surfacearea_sphere('five')

    def test_edge_case_large_input(self):
        self.assertAlmostEqual(surfacearea_sphere(100), 12566.536872745432)
