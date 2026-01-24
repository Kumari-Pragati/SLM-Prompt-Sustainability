import unittest
from mbpp_731_code import math, pi, sqrt
from your_module import lateralsurface_cone  # replace 'your_module' with the actual module name where the function is defined

class TestLateralSurfaceCone(unittest.TestCase):

    def test_lateralsurface_cone_with_positive_values(self):
        self.assertAlmostEqual(lateralsurface_cone(1, 2), 12.566370614359172)
        self.assertAlmostEqual(lateralsurface_cone(2, 3), 37.7110735988076)
        self.assertAlmostEqual(lateralsurface_cone(3, 4), 113.09762806451614)

    def test_lateralsurface_cone_with_zero_radius(self):
        with self.assertRaises(ValueError):
            lateralsurface_cone(0, 1)

    def test_lateralsurface_cone_with_negative_values(self):
        with self.assertRaises(ValueError):
            lateralsurface_cone(-1, 2)
        with self.assertRaises(ValueError):
            lateralsurface_cone(1, -2)
