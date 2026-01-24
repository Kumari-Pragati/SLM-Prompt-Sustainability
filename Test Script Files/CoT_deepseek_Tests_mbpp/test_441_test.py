import unittest
from mbpp_441_code import surfacearea_cube

class TestSurfaceAreaCube(unittest.TestCase):

    def test_positive_length(self):
        self.assertEqual(surfacearea_cube(3), 54)
        self.assertEqual(surfacearea_cube(5), 150)

    def test_zero_length(self):
        self.assertEqual(surfacearea_cube(0), 0)

    def test_negative_length(self):
        with self.assertRaises(ValueError):
            surfacearea_cube(-3)

    def test_non_integer_length(self):
        with self.assertRaises(TypeError):
            surfacearea_cube(3.5)
