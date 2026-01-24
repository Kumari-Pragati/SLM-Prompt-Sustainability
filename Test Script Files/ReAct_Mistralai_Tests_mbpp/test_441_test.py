import unittest
from mbpp_441_code import surfacearea_cube

class TestSurfaceAreaCube(unittest.TestCase):

    def test_positive_integer(self):
        "Test surface area calculation for positive integers"
        self.assertEqual(surfacearea_cube(3), 54)

    def test_zero(self):
        "Test surface area calculation for zero"
        self.assertEqual(surfacearea_cube(0), 0)

    def test_negative_integer(self):
        "Test surface area calculation for negative integers"
        self.assertEqual(surfacearea_cube(-1), 6)

    def test_float(self):
        "Test surface area calculation for float values"
        self.assertAlmostEqual(surfacearea_cube(2.5), 106.25)

    def test_non_numeric(self):
        "Test surface area calculation for non-numeric values"
        with self.assertRaises(TypeError):
            surfacearea_cube("not a number")
