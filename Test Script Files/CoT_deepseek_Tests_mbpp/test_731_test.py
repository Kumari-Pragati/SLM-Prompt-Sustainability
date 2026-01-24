import unittest
from mbpp_731_code import lateralsurface_cone

class TestLatersurfaceCone(unittest.TestCase):

    def test_typical_case(self):
        self.assertAlmostEqual(lateralsurface_cone(5, 12), 261.7993877991494)

    def test_zero_radius(self):
        self.assertEqual(lateralsurface_cone(0, 10), 0)

    def test_zero_height(self):
        self.assertEqual(lateralsurface_cone(5, 0), 0)

    def test_negative_radius(self):
        with self.assertRaises(ValueError):
            lateralsurface_cone(-5, 10)

    def test_negative_height(self):
        with self.assertRaises(ValueError):
            lateralsurface_cone(5, -10)

    def test_large_numbers(self):
        self.assertAlmostEqual(lateralsurface_cone(10000, 20000), 1.2566370614359173e+10)
