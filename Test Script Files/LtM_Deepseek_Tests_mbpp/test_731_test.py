import unittest
from mbpp_731_code import lateralsurface_cone

class TestLatersurfaceCone(unittest.TestCase):

    def test_typical_case(self):
        self.assertAlmostEqual(lateralsurface_cone(5, 12), 226.1946710584651)

    def test_small_radius(self):
        self.assertAlmostEqual(lateralsurface_cone(0.1, 10), 3.141592653589793)

    def test_large_radius(self):
        self.assertAlmostEqual(lateralsurface_cone(1000, 2000), 12566370.614359173)

    def test_small_height(self):
        self.assertAlmostEqual(lateralsurface_cone(5, 0.1), 0.7853981633974483)

    def test_large_height(self):
        self.assertAlmostEqual(lateralsurface_cone(5, 1000), 31415.92653589793)

    def test_negative_radius(self):
        with self.assertRaises(ValueError):
            lateralsurface_cone(-5, 10)

    def test_negative_height(self):
        with self.assertRaises(ValueError):
            lateralsurface_cone(5, -10)

    def test_zero_radius(self):
        self.assertEqual(lateralsurface_cone(0, 10), 0)

    def test_zero_height(self):
        self.assertEqual(lateralsurface_cone(5, 0), 0)
