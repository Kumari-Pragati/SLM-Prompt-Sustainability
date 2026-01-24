import unittest
from mbpp_441_code import surfacearea_cube

class TestSurfaceAreaCube(unittest.TestCase):
    def test_positive_integer(self):
        self.assertEqual(surfacearea_cube(3), 54)

    def test_zero(self):
        self.assertEqual(surfacearea_cube(0), 0)

    def test_negative_number(self):
        self.assertEqual(surfacearea_cube(-1), math.nan)

    def test_float_number(self):
        self.assertAlmostEqual(surfacearea_cube(2.5), 106.25)

    def test_string_input(self):
        self.assertRaises(TypeError, surfacearea_cube, "not a number")

    def test_list_input(self):
        self.assertRaises(TypeError, surfacearea_cube, [1, 2, 3])
