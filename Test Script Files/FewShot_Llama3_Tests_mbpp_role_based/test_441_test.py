import unittest
from mbpp_441_code import surfacearea_cube

class TestSurfaceareaCube(unittest.TestCase):
    def test_positive_length(self):
        self.assertEqual(surfacearea_cube(5), 900)

    def test_zero_length(self):
        self.assertEqual(surfacearea_cube(0), 0)

    def test_negative_length(self):
        with self.assertRaises(TypeError):
            surfacearea_cube(-5)

    def test_non_numeric_input(self):
        with self.assertRaises(TypeError):
            surfacearea_cube('five')
