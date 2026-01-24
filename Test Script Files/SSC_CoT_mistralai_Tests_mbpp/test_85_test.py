import unittest
from mbpp_85_code import surfacearea_sphere

class TestSurfaceAreaSphere(unittest.TestCase):
    def test_normal_input(self):
        self.assertEqual(surfacearea_sphere(3), 4 * math.pi * 3 * 3)

    def test_edge_cases(self):
        self.assertAlmostEqual(surfacearea_sphere(0), 0)
        self.assertAlmostEqual(surfacearea_sphere(1e-8), 4 * math.pi * 1e-16)

    def test_negative_input(self):
        with self.assertRaises(ValueError):
            surfacearea_sphere(-1)

    def test_non_numeric_input(self):
        with self.assertRaises(TypeError):
            surfacearea_sphere('str')
