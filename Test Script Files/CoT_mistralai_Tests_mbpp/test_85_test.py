import unittest
from mbpp_85_code import surfacearea_sphere

class TestSurfaceAreaSphere(unittest.TestCase):
    def test_positive_number(self):
        self.assertAlmostEqual(surfacearea_sphere(3), 113.097265625)

    def test_zero(self):
        self.assertEqual(surfacearea_sphere(0), 0.0)

    def test_negative_number(self):
        with self.assertRaises(ValueError):
            surfacearea_sphere(-1)

    def test_non_numeric_input(self):
        with self.assertRaises(TypeError):
            surfacearea_sphere('str')
