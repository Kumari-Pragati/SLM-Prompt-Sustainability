import unittest
from mbpp_266_code import lateralsurface_cube

class TestLateralSurfaceCube(unittest.TestCase):
    def test_positive_integer(self):
        self.assertEqual(lateralsurface_cube(3), 36)
        self.assertEqual(lateralsurface_cube(5), 100)
        self.assertEqual(lateralsurface_cube(10), 400)

    def test_zero(self):
        self.assertEqual(lateralsurface_cube(0), 0)

    def test_negative_integer(self):
        self.assertEqual(lateralsurface_cube(-1), 1)
        self.assertEqual(lateralsurface_cube(-3), 36)
        self.assertEqual(lateralsurface_cube(-5), 100)

    def test_float(self):
        self.assertAlmostEqual(lateralsurface_cube(2.5), 35)
        self.assertAlmostEqual(lateralsurface_cube(4.5), 108)
        self.assertAlmostEqual(lateralsurface_cube(6.5), 130)

    def test_non_numeric(self):
        self.assertRaises(TypeError, lateralsurface_cube, 'str')
        self.assertRaises(TypeError, lateralsurface_cube, None)
        self.assertRaises(TypeError, lateralsurface_cube, [1, 2, 3])
