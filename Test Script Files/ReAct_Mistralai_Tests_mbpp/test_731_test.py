import unittest
from mbpp_731_code import lateralsurface_cone

class TestLateralSurfaceCone(unittest.TestCase):

    def test_positive_values(self):
        self.assertAlmostEqual(lateralsurface_cone(1, 2), math.pi * 3)
        self.assertAlmostEqual(lateralsurface_cone(3, 4), math.pi * math.sqrt(10) * 5)

    def test_zero_radius(self):
        with self.assertRaises(ValueError):
            lateralsurface_cone(0, 1)

    def test_negative_radius(self):
        with self.assertRaises(ValueError):
            lateralsurface_cone(-1, 1)

    def test_zero_height(self):
        self.assertEqual(lateralsurface_cone(1, 0), math.pi)

    def test_negative_height(self):
        with self.assertRaises(ValueError):
            lateralsurface_cone(1, -1)

    def test_large_values(self):
        self.assertAlmostEqual(lateralsurface_cone(1e6, 1e6), math.pi * 1e6 * math.sqrt(2 * 1e6))
