import unittest
from mbpp_379_code import surfacearea_cuboid

class TestSurfaceAreaCuboid(unittest.TestCase):

    def test_positive_numbers(self):
        """Test surface area calculation with positive numbers."""
        self.assertEqual(surfacearea_cuboid(2, 3, 4), 108)
        self.assertEqual(surfacearea_cuboid(5, 10, 15), 1300)

    def test_zero_length(self):
        """Test surface area calculation with zero length."""
        self.assertEqual(surfacearea_cuboid(0, 3, 4), 36)
        self.assertEqual(surfacearea_cuboid(0, 0, 5), 0)

    def test_negative_numbers(self):
        """Test surface area calculation with negative numbers."""
        self.assertEqual(surfacearea_cuboid(-2, -3, -4), 108)
        self.assertRaises(ValueError, surfacearea_cuboid, -5, 10, -15)

    def test_float_numbers(self):
        """Test surface area calculation with float numbers."""
        self.assertAlmostEqual(surfacearea_cuboid(2.5, 3.2, 4.1), 111.68, delta=1)
        self.assertAlmostEqual(surfacearea_cuboid(5.0, 10.0, 15.0), 1300.0, delta=1)
