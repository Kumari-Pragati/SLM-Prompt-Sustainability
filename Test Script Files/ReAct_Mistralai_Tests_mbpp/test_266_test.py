import unittest
from mbpp_266_code import lateralsurface_cube

class TestLateralSurfaceCube(unittest.TestCase):

    def test_positive_integer(self):
        """Test lateralsurface_cube with positive integer"""
        self.assertEqual(lateralsurface_cube(3), 36)

    def test_zero(self):
        """Test lateralsurface_cube with zero"""
        self.assertEqual(lateralsurface_cube(0), 0)

    def test_negative_integer(self):
        """Test lateralsurface_cube with negative integer"""
        self.assertEqual(lateralsurface_cube(-1), 1)

    def test_float(self):
        """Test lateralsurface_cube with float"""
        self.assertAlmostEqual(lateralsurface_cube(2.5), 25)

    def test_non_numeric(self):
        """Test lateralsurface_cube with non-numeric input"""
        self.assertRaises(TypeError, lateralsurface_cube, 'str')
