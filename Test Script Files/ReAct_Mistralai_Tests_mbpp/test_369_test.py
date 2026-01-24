import unittest
from mbpp_369_code import lateralsurface_cuboid

class TestLateralSurfaceCuboid(unittest.TestCase):

    def test_positive_typical_case(self):
        # Typical case: positive lengths
        self.assertEqual(lateralsurface_cuboid(3, 4, 5), 68)

    def test_zero_length(self):
        # Edge case: zero length
        self.assertEqual(lateralsurface_cuboid(0, 4, 5), 0)

    def test_negative_length(self):
        # Edge case: negative lengths
        self.assertEqual(lateralsurface_cuboid(-3, 4, 5), 48)
        self.assertEqual(lateralsurface_cuboid(3, -4, 5), 48)
        self.assertEqual(lateralsurface_cuboid(3, 4, -5), 0)

    def test_negative_width(self):
        # Edge case: negative width
        self.assertEqual(lateralsurface_cuboid(3, -4, 5), 48)

    def test_negative_height(self):
        # Edge case: negative height
        self.assertEqual(lateralsurface_cuboid(3, 4, -5), 0)

    def test_float_length(self):
        # Edge case: float lengths
        self.assertAlmostEqual(lateralsurface_cuboid(3.1, 4, 5), 68.2)

    def test_invalid_input(self):
        # Error case: invalid input (non-numeric)
        with self.assertRaises(TypeError):
            lateralsurface_cuboid('a', 4, 5)
        with self.assertRaises(TypeError):
            lateralsurface_cuboid(3, 'a', 5)
        with self.assertRaises(TypeError):
            lateralsurface_cuboid(3, 4, 'a')
